from textnode import *


def main():
    old_node = TextNode(
    "This is a text with an image ![alt text](image.jpg) and some text with another one ![alt text number 2](image_number_2.jpg) and another other one ![test3](image_test_3.jpg)",
    TextType.TEXT,
    )
    print(split_nodes_images([old_node]))



if __name__ == "__main__":
    main()
