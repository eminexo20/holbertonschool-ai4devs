import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestMalformed(unittest.TestCase):
    def test_malformed_lines_counted(self):
        analyzer = LogAnalyzer()
        logs = "\n".join([
            "CORRUPTED_LINE_WITHOUT_STRUCTURE",
            '192.168.0.5 - - [15/Nov/2026:12:05:00 +0000] "GET /health HTTP/1.1" 200 64',
        ])
        result = analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["malformed_entries"], 1)


if __name__ == "__main__":
    unittest.main()
