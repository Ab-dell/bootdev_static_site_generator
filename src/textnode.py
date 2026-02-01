from enum import Enum
from htmlnode import LeafNode
import re


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGES = "images"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    
    def __eq__(self, other):
        return (self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url)
            
        
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGES:
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        case _:
            raise ValueError(f"invalid text type: {text_node.text_type}")



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
        list_of_images_in_text = extract_markdown_links(node.text)

        if node.text == "":
            continue

        if len(list_of_images_in_text) == 0:
            new_nodes.append(node)
            continue

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        
        link_text = list_of_images_in_text[0][0]
        link_url = list_of_images_in_text[0][1]
        link_mardown_text = f"[{link_text}]({link_url})"
        list_of_images_in_text.remove(list_of_images_in_text[0])

        text_to_check_list = node.text.split(link_mardown_text, 1)

            
        if text_to_check_list[0] == "":
            continue
            
        new_nodes.append(TextNode(text_to_check_list[0], TextType.TEXT))
        new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

        remainder = text_to_check_list[1]
        if remainder != "":
            new_nodes.extend(split_nodes_links([TextNode(text_to_check_list[1], TextType.TEXT)]))

        
    return new_nodes


        
    
    
    
    
        
    