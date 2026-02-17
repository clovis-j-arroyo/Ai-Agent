import os

def get_files_info(working_directory, directory="."):
    try:
        absolute_directory = os.path.abspath(working_directory)
        target_dir  = os.path.normpath(os.path.join(absolute_directory, directory))

        valid_target_dir = os.path.commonpath([absolute_directory, target_dir]) == absolute_directory

        directory_checker = os.path.isdir(target_dir)

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not directory_checker:
            return f'Error: "{directory}" is not a directory'
        

        dir_list = []
        for item in os.listdir(target_dir):
            full_path = os.path.join(target_dir, item)
            size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)
            dir_list.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(dir_list)
    except Exception as e:
        return f"Error: {e}"
