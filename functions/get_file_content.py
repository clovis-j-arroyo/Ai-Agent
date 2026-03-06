import os
from config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the file contents of a specified file relative to the working directory",
    parameters=types.Schema(
        required= ["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path, relative to the working directory ",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):

    try:
        absolute_working_dir = os.path.abspath(working_directory)
        absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))


        if os.path.commonpath([absolute_working_dir, absolute_file_path]) != absolute_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        
        elif not os.path.isfile(absolute_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(absolute_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f'Error: {e}'