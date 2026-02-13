from block_elements import *
from split_node import text_to_textnodes
from textnode import TextNode,TextType, text_node_to_html_node
from htmlnode import ParentNode, LeafNode



#helper function to get all children of an HTMLnode
def text_to_children(text):
    list_of_children = []
    list_of_text_nodes_from_text = text_to_textnodes(text)
    for node in list_of_text_nodes_from_text:
        list_of_children.append(text_node_to_html_node(node))

    return list_of_children
    

def markdown_to_html_node(markdown):
    all_html_nodes = []
    list_of_blocks_from_markdown = markdown_to_blocks(markdown)
    
    for block in list_of_blocks_from_markdown:
        block_type = block_to_block_type(block)
        
        if block != None:
            if block_type == BlockType.PARAGRAPH:
                html_node_from_block = ParentNode("p", text_to_children(block.replace("\n", " ")))

            elif block_type == BlockType.HEADING:
                count = 0
                for char in block:
                    if char == "#":
                        count += 1
                    else:
                        break
                html_node_from_block = ParentNode(f"h{count}", text_to_children(block[count + 1:]))

            elif block_type == BlockType.CODE:
                html_node_from_block = ParentNode("pre", [
                    text_node_to_html_node(TextNode(block[4:-3], TextType.CODE))
                    ]
                )

            elif block_type == BlockType.QUOTE:
                quote =""
                for line in block.split("\n"):
                    quote += line.strip("> ") + " "

                html_node_from_block = ParentNode("blockquote", text_to_children(quote.strip()))

            elif block_type == BlockType.ORDERED_LIST:
                children = []
                for list_item in block.split("\n"):
                    children.append(ParentNode("li", text_to_children(list_item[3:]) ) )

                html_node_from_block = ParentNode("ol", children)
                
            elif block_type == BlockType.UNORDERED_LIST:
                children = []
                for list_item in block.split("\n"):
                    children.append(ParentNode("li", text_to_children(list_item[2:]) ) )

                html_node_from_block = ParentNode("ul", children)

        all_html_nodes.append(html_node_from_block)

    return ParentNode("div", all_html_nodes)
            