import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestInvalidStatus(unittest.TestCase):
    def test_invalid_http_status_range(self):
        analyzer = LogAnalyzer()
        log = '10.0.0.1 - - [15/Nov/2026:12:20:00 +0000] "GET /test HTTP/1.1" 999 100'
        result = analyzer.analyze(log)
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["malformed_entries"], 1)


if __name__ == "__main__":
    unittest.main()
