import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestListInput(unittest.TestCase):
    def test_list_input_supported(self):
        analyzer = LogAnalyzer()
        lines = [
            '10.0.0.1 - - [15/Nov/2026:12:25:00 +0000] "GET /a HTTP/1.1" 200 50',
            '10.0.0.2 - - [15/Nov/2026:12:25:01 +0000] "GET /b HTTP/1.1" 201 75',
        ]
        result = analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["total_bytes"], 125)


if __name__ == "__main__":
    unittest.main()
