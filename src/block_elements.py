



def markdown_to_blocks(markdown):
    list_of_block = []

    for block in markdown.split("\n\n"):
        if block == "":
            continue
        list_of_block.append(block.strip())
        

    return list_of_block