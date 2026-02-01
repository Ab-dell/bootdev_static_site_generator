from textnode import *


def main():
    old_node = TextNode(
    "![image](https://www.example.COM/IMAGE.PNG)",
    TextType.TEXT,
)
    print(split_nodes_images([old_node]))



if __name__ == "__main__":
    main()
