import unittest
from block_elements import *




class TestBlockElements(unittest.TestCase):
    def test_mardown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_mardown_to_blocks_2(self):
            md = """
This is a `code` word

blablabla

tooooooooooooozzzz

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is a `code` word",
                    "blablabla",
                    "tooooooooooooozzzz",
                    "- This is a list\n- with items",
                ],
            )

    
    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_paragraph(self):
         markdown = "this just a paragraph\n albeit multiline one"
         self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
         markdown = "```\nthis just a code block\n albeit multiline one```"
         self.assertEqual(block_to_block_type(markdown), BlockType.CODE)

    def test_block_to_block_type_quote(self):
         markdown = "> blockquote"
         self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)
    
    def test_block_to_block_type_quote_no_space(self):
         markdown = ">blockquote"
         self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)

    def test_block_to_block_type_unordered_list_one_line(self):
         markdown = "- an item in a list"
         self.assertEqual(block_to_block_type(markdown), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_unordered_list_multiple_line(self):
         markdown = """- an item in a list\n- another one\n- and another one """
         self.assertEqual(block_to_block_type(markdown), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list_one_line(self):
         markdown = """1. an item in a list\n2. another one\n3. and another one """
         self.assertEqual(block_to_block_type(markdown), BlockType.ORDERED_LIST)



if __name__ == "__main__":
    unittest.main()