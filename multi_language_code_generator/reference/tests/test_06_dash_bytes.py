import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestDashBytes(unittest.TestCase):
    def test_dash_bytes_parsed_as_zero(self):
        analyzer = LogAnalyzer()
        log = '172.16.0.1 - - [15/Nov/2026:12:10:00 +0000] "DELETE /api/item/9 HTTP/1.1" 404 -'
        result = analyzer.analyze(log)
        self.assertEqual(result["total_bytes"], 0)
        self.assertEqual(result["error_rate"], 100.0)


if __name__ == "__main__":
    unittest.main()
