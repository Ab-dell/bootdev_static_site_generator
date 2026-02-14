from textnode import *
from split_node import *
from block_elements import markdown_to_blocks
from markdown_to_html_node import markdown_to_html_node
from generate_page import copy_content, generate_page, generate_pages_recursive


def main():
    copy_content("static","public")
    generate_pages_recursive("content", "template.html", "public")



if __name__ == "__main__":
    main()
