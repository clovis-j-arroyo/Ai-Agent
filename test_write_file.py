from functions.file_writer import write_file

print("FIRST TEST:")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print("NEXT TEST:")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print("NEXT TEST:")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
