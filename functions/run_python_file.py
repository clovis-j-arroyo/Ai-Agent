import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_dir = os.path.abspath(working_directory) 
        abs_file = os.path.abspath(os.path.join(working_directory, file_path))

        if os.path.commonpath([abs_dir, abs_file]) != abs_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
        if not os.path.isfile(abs_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not abs_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_file]

        if args:
            command.extend(args)

        result = subprocess.run(command, cwd=abs_dir, capture_output=True, text=True, timeout=30)
        output_line = []

        if result.returncode != 0:
            output_line.append(f"Process exited with code {result.returncode}")

        if not result.stdout and not result.stderr:
            output_line.append("No output produced")
        
        if result.stdout:
            output_line.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output_line.append(f"STDERR:\n{result.stderr}")
            
        return "\n".join(output_line)

    except Exception as e:
        return f"Error: executing Python file: {e}"