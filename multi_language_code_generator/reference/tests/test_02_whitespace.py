import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestWhitespace(unittest.TestCase):
    def test_whitespace_only(self):
        analyzer = LogAnalyzer()
        result = analyzer.analyze("   \n\t\n  ")
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["malformed_entries"], 0)


if __name__ == "__main__":
    unittest.main()
