from functions.get_file_content import get_file_content

print("FIRST TEST HERE:")
print(get_file_content("calculator", "lorem.txt"))

print("NEXT TEXT:")
print(get_file_content("calculator", "main.py"))

print("NEXT TEXT:")
print(get_file_content("calculator", "pkg/calculator.py"))

print("NEXT TEXT:")
print(get_file_content("calculator", "/bin/cat"))

print("NEXT TEXT:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
