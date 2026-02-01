from textnode import *


def main():
    old_node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
    print(split_nodes_links([old_node]))



if __name__ == "__main__":
    main()
