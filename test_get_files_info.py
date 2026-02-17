from functions.get_files_info import get_files_info

print("THIS IS THE FIRST TEST:")
print(get_files_info("calculator", "."))

print("NEXT TEXT:")
print(get_files_info("calculator", "pkg"))

print("NEXT TEXT:")
print(get_files_info("calculator", "/bin"))

print("NEXT TEXT:")
print(get_files_info("calculator", "../"))