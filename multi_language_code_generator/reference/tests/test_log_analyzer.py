import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from log_analyzer import LogAnalyzer


class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_01_empty_string(self):
        result = self.analyzer.analyze("")
        self.assertEqual(
            result,
            {
                "total_requests": 0,
                "unique_visitors": 0,
                "error_rate": 0.0,
                "total_bytes": 0,
                "top_endpoint": None,
                "malformed_entries": 0,
            },
        )

    def test_02_whitespace_only(self):
        result = self.analyzer.analyze("   \n\t\n  ")
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["malformed_entries"], 0)

    def test_03_single_valid_request(self):
        log = '192.168.1.1 - - [15/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 1024'
        result = self.analyzer.analyze(log)
        self.assertEqual(
            result,
            {
                "total_requests": 1,
                "unique_visitors": 1,
                "error_rate": 0.0,
                "total_bytes": 1024,
                "top_endpoint": "/home",
                "malformed_entries": 0,
            },
        )

    def test_04_standard_mixed_traffic(self):
        logs = "\n".join([
            '10.0.0.1 - - [15/Nov/2026:12:00:01 +0000] "GET /index.html HTTP/1.1" 200 2048',
            '10.0.0.2 - - [15/Nov/2026:12:00:02 +0000] "POST /api/login HTTP/1.1" 401 512',
            '10.0.0.1 - - [15/Nov/2026:12:00:03 +0000] "GET /index.html HTTP/1.1" 200 2048',
            '10.0.0.3 - - [15/Nov/2026:12:00:04 +0000] "GET /dashboard HTTP/1.1" 500 256',
        ])
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 4)
        self.assertEqual(result["unique_visitors"], 3)
        self.assertEqual(result["error_rate"], 50.0)
        self.assertEqual(result["total_bytes"], 4864)
        self.assertEqual(result["top_endpoint"], "/index.html")

    def test_05_malformed_lines_counted(self):
        logs = "\n".join([
            "CORRUPTED_LINE_WITHOUT_STRUCTURE",
            '192.168.0.5 - - [15/Nov/2026:12:05:00 +0000] "GET /health HTTP/1.1" 200 64',
            '192.168.0.6 - - [15/Nov/2026:12:05:01 +0000] "GET /broken HTTP/1.1" NOT_A_CODE 100',
        ])
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["malformed_entries"], 2)

    def test_06_dash_bytes_parsed_as_zero(self):
        logs = "\n".join([
            '172.16.0.1 - - [15/Nov/2026:12:10:00 +0000] "DELETE /api/item/9 HTTP/1.1" 404 -',
            '172.16.0.1 - - [15/Nov/2026:12:10:05 +0000] "GET /api/secret HTTP/1.1" 403 128',
        ])
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_bytes"], 128)
        self.assertEqual(result["error_rate"], 100.0)

    def test_07_endpoint_tie_breaking_lexicographical(self):
        logs = "\n".join([
            '10.1.1.1 - - [15/Nov/2026:12:15:00 +0000] "GET /zebra HTTP/1.1" 200 100',
            '10.1.1.2 - - [15/Nov/2026:12:15:01 +0000] "GET /alpha HTTP/1.1" 200 100',
        ])
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["top_endpoint"], "/alpha")

    def test_08_invalid_http_status_range(self):
        log = '10.0.0.1 - - [15/Nov/2026:12:20:00 +0000] "GET /test HTTP/1.1" 999 100'
        result = self.analyzer.analyze(log)
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["malformed_entries"], 1)

    def test_09_list_input_supported(self):
        lines = [
            '10.0.0.1 - - [15/Nov/2026:12:25:00 +0000] "GET /a HTTP/1.1" 200 50',
            '10.0.0.2 - - [15/Nov/2026:12:25:01 +0000] "GET /b HTTP/1.1" 201 75',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["total_bytes"], 125)

    def test_10_error_rate_rounding(self):
        logs = "\n".join([
            '10.0.0.1 - - [15/Nov/2026:12:30:00 +0000] "GET /ok1 HTTP/1.1" 200 10',
            '10.0.0.2 - - [15/Nov/2026:12:30:01 +0000] "GET /ok2 HTTP/1.1" 200 10',
            '10.0.0.3 - - [15/Nov/2026:12:30:02 +0000] "GET /err HTTP/1.1" 502 10',
        ])
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["error_rate"], 33.33)


if __name__ == "__main__":
    unittest.main()
