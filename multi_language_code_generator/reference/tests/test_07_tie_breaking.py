import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestTieBreaking(unittest.TestCase):
    def test_endpoint_tie_breaking(self):
        analyzer = LogAnalyzer()
        logs = "\n".join([
            '10.1.1.1 - - [15/Nov/2026:12:15:00 +0000] "GET /zebra HTTP/1.1" 200 100',
            '10.1.1.2 - - [15/Nov/2026:12:15:01 +0000] "GET /alpha HTTP/1.1" 200 100',
        ])
        result = analyzer.analyze(logs)
        self.assertEqual(result["top_endpoint"], "/alpha")


if __name__ == "__main__":
    unittest.main()
