from textnode import TextNode, TextType, split_nodes_delimiter, extract_markdown_images


def main():
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a second ![un bg de ouf](https://i.imgur.com/aaaaa.png)"
    print(extract_markdown_images(text))



if __name__ == "__main__":
    main()
