import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestMixedTraffic(unittest.TestCase):
    def test_standard_mixed_traffic(self):
        analyzer = LogAnalyzer()
        logs = "\n".join([
            '10.0.0.1 - - [15/Nov/2026:12:00:01 +0000] "GET /index.html HTTP/1.1" 200 2048',
            '10.0.0.2 - - [15/Nov/2026:12:00:02 +0000] "POST /api/login HTTP/1.1" 401 512',
        ])
        result = analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["error_rate"], 50.0)


if __name__ == "__main__":
    unittest.main()
