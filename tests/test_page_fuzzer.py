import unittest
from unittest.mock import patch, mock_open
import page_fuzzer

class TestFuzzAllPages(unittest.TestCase):
    def test_reads_multiple_lines(self):
        sample = "one\nsecond\n"
        with patch("builtins.open", mock_open(read_data=sample)):
            with patch("requests.get") as mock_get:
                mock_get.return_value.status_code = 200
                results = page_fuzzer.fuzzallpages("http://example.com/")
        self.assertEqual(len(results), 2)

if __name__ == "__main__":
    unittest.main()
