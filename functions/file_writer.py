import os
from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes a files to a specified file path relative to the working directory",
    parameters=types.Schema(
        required=["file_path","content"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path, relative to the working directory ",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="contents that will be written on the given file",
            )
        },
    ),
)


def write_file(working_directory, file_path, content):
    try:
        absolute_dir= os.path.abspath(working_directory)
        absolute_file= os.path.abspath(os.path.join(working_directory, file_path))

        if os.path.commonpath([absolute_dir,absolute_file]) != absolute_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(absolute_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(os.path.dirname(absolute_file), exist_ok=True)
        with open(absolute_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'