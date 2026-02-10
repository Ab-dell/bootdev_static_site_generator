from textnode import *
from split_node import *
from block_elements import markdown_to_blocks
from mardown_to_html_node import markdown_to_html_node


def main():
    md = """
This is a **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    print(markdown_to_html_node(md))



if __name__ == "__main__":
    main()
