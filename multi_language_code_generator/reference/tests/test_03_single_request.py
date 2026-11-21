import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestSingleRequest(unittest.TestCase):
    def test_single_valid_request(self):
        analyzer = LogAnalyzer()
        log = '192.168.1.1 - - [15/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 1024'
        result = analyzer.analyze(log)
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["top_endpoint"], "/home")


if __name__ == "__main__":
    unittest.main()
