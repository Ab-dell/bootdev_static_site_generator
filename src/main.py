import sys
from textnode import *
from split_node import *
from block_elements import markdown_to_blocks
from markdown_to_html_node import markdown_to_html_node
from generate_page import copy_content, generate_page, generate_pages_recursive


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_content("static","docs")
<<<<<<< HEAD
    generate_pages_recursive("content", "template.html", "docs", basepath)
=======
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)
>>>>>>> 78f7b5c8d260e9b4fa35ac16860d842bfe65d9ff



if __name__ == "__main__":
    main()
