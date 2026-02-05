import re
from enum import Enum



class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    

def markdown_to_blocks(markdown):
    list_of_block = []

    for block in markdown.split("\n\n"):
        if block == "":
            continue
        list_of_block.append(block.strip())
        

    return list_of_block


def block_to_block_type(markdown_block):
    
    heading_regex = r"^#{1,6}\s.+"
    multiline_block_list = markdown_block.split("\n")


    if re.match(heading_regex, markdown_block):
        return BlockType.HEADING
    elif markdown_block.startswith("```\n") and markdown_block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") or line.startswith("> ") for line in multiline_block_list):
        return BlockType.QUOTE
    elif all(line.startswith(f"- ") for line in multiline_block_list):
        return BlockType.UNORDERED_LIST
    else:   
        for index, line in enumerate(multiline_block_list):
            if not line.startswith(f"{index +1 }. "):
                return BlockType.PARAGRAPH
            
        return BlockType.ORDERED_LIST
        
