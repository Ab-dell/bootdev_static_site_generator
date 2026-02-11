import os
import shutil



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