import re
from textnode import TextType, TextNode




def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        
        text_to_check_list = node.text.split(delimiter)
        if len(text_to_check_list) % 2 == 0:
            raise Exception("No closing delimiter was found")
            
        for i in range(len(text_to_check_list)):
            if text_to_check_list[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text_to_check_list[i], TextType.TEXT))
            elif i % 2 == 1:
                new_nodes.append(TextNode(text_to_check_list[i], text_type))
                    
        
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_images(old_nodes):
    new_nodes = []

    for node in old_nodes:
        list_of_images_in_text = extract_markdown_images(node.text)

        if node.text == "":
            continue

        if len(list_of_images_in_text) == 0:
            new_nodes.append(node)
            continue

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        
        image_alt = list_of_images_in_text[0][0]
        image_url = list_of_images_in_text[0][1]
        image_mardown_text = f"![{image_alt}]({image_url})"
        list_of_images_in_text.remove(list_of_images_in_text[0])

        text_to_check_list = node.text.split(image_mardown_text, 1)

            
        if text_to_check_list[0] == "":
            new_nodes.append(TextNode(image_alt, TextType.IMAGES, image_url))
            continue
            
        new_nodes.append(TextNode(text_to_check_list[0], TextType.TEXT))
        new_nodes.append(TextNode(image_alt, TextType.IMAGES, image_url))

        remainder = text_to_check_list[1]
        if remainder != "":
            new_nodes.extend(split_nodes_images([TextNode(text_to_check_list[1], TextType.TEXT)]))

        
    return new_nodes



def split_nodes_links(old_nodes):
    new_nodes = []

    for node in old_nodes:
        list_of_links_in_text = extract_markdown_links(node.text)

        if node.text == "":
            continue

        if len(list_of_links_in_text) == 0:
            new_nodes.append(node)
            continue

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        
        link_text = list_of_links_in_text[0][0]
        link_url = list_of_links_in_text[0][1]
        link_mardown_text = f"[{link_text}]({link_url})"
        list_of_links_in_text.remove(list_of_links_in_text[0])

        text_to_check_list = node.text.split(link_mardown_text, 1)

            
        if text_to_check_list[0] == "":
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            continue
            
        new_nodes.append(TextNode(text_to_check_list[0], TextType.TEXT))
        new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

        remainder = text_to_check_list[1]
        if remainder != "":
            new_nodes.extend(split_nodes_links([TextNode(text_to_check_list[1], TextType.TEXT)]))

        
    return new_nodes


def text_to_textnodes(text):
    text_node = [TextNode(text, TextType.TEXT)]

    list_of_nodes_without_links_or_images_checked = split_nodes_delimiter(
        split_nodes_delimiter(
        split_nodes_delimiter(text_node,"**", TextType.BOLD),
        "_",
        TextType.ITALIC
    ), "`", TextType.CODE)

    list_of_nodes_with_all_but_links_checked = split_nodes_images(list_of_nodes_without_links_or_images_checked)
    list_of_nodes_with_everything_checked = split_nodes_links(list_of_nodes_with_all_but_links_checked)

    return list_of_nodes_with_everything_checked