import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestRounding(unittest.TestCase):
    def test_error_rate_rounding(self):
        analyzer = LogAnalyzer()
        logs = "\n".join([
            '10.0.0.1 - - [15/Nov/2026:12:30:00 +0000] "GET /ok1 HTTP/1.1" 200 10',
            '10.0.0.2 - - [15/Nov/2026:12:30:01 +0000] "GET /ok2 HTTP/1.1" 200 10',
            '10.0.0.3 - - [15/Nov/2026:12:30:02 +0000] "GET /err HTTP/1.1" 502 10',
        ])
        result = analyzer.analyze(logs)
        self.assertEqual(result["error_rate"], 33.33)


if __name__ == "__main__":
    unittest.main()
