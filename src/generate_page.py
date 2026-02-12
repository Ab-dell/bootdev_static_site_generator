from block_elements import markdown_to_blocks



def extract_title(markdown):
    list_of_blocks = markdown_to_blocks(markdown)

    for block in list_of_blocks:
        if block.startswith("#"):
            return block.strip("#").strip()
        else:
            raise Exception("Error: No title was found")



def generate_page(from_path, template_path, dest_path):
    pass