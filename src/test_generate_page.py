import unittest
from generate_page import extract_title



class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual("Hello", extract_title("# Hello"))

    def test_extract_title_with_whotespaces(self):
        self.assertEqual("The Hobbit", extract_title("# The Hobbit"))

    def test_extract_title_multiple_lines(self):
        document = """
# My Adventure

This is a story about a bear and a wizard.
"""
        self.assertEqual("My Adventure", extract_title(document))





if __name__ == "__main__":
    unittest.main()