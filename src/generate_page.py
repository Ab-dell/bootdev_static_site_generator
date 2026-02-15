import os
import shutil
import pathlib
from block_elements import markdown_to_blocks
from markdown_to_html_node import markdown_to_html_node



def copy_content(source_dir_path, destination_dir_path):
    # source_dir_abs_path = os.path.abspath(source_dir_path)
    # destination_dir_abs_path = os.path.abspath(destination_dir_path)
    try:
        if not os.path.exists(source_dir_path):
            raise Exception("Error: The source directory does not exist")
        
        if os.path.exists(destination_dir_path):
            shutil.rmtree(destination_dir_path)
        
        os.mkdir(destination_dir_path)

        for file in os.listdir(source_dir_path):
            current_file = os.path.join(source_dir_path, file)

            if not os.path.exists(current_file):
                print(f"Error: {current_file} is does not exist")
                continue

            if os.path.isdir(current_file):
                copy_content(current_file, os.path.join(destination_dir_path, file))
                continue

            print(f"copiying {current_file}")
            shutil.copy(current_file, destination_dir_path)

        
    except Exception as e:
        return f"Error: {e}"


def extract_title(markdown):
    list_of_blocks = markdown_to_blocks(markdown)

    for block in list_of_blocks:
        if block.startswith("#"):
            return block.strip("#").strip()
        else:
            raise Exception("Error: No title was found")



def generate_page(from_path, template_path, dest_path):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as src_file:
        src_file_content = src_file.read()

    html_string_from_markdown = markdown_to_html_node(src_file_content).to_html()
    title_of_page = extract_title(src_file_content)

    with open(template_path, "r") as template_file:
        template_file_content = template_file.read()

        template_file_content = template_file_content.replace("{{ Title }}", title_of_page)
        template_file_content = template_file_content.replace("{{ Content }}", html_string_from_markdown)
        template_file_content = template_file_content.replace('href="/', 'href="{basepath}')
        template_file_content = template_file_content.replace('src="/', 'src="{basepath}')

    if os.path.dirname(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template_file_content)



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        current_file = os.path.join(dir_path_content, file)
        if not os.path.isfile(current_file):
            generate_pages_recursive(current_file, template_path, os.path.join(dest_dir_path, file))
            
        else:
            generate_page(current_file, template_path, pathlib.Path(os.path.join(dest_dir_path, file)).with_suffix(".html") )
        

        


    

    

    


    