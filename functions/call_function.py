from functions.get_files_info import schema_get_files_info
import types

available_functions = types.Tool(
    function_declarations=[schema_get_files_info],
)