with open("file io\demo.txt", "r") as f:
    content = f.read()
    print(content)

with open("file io\demo.txt", "w") as f:
    f.write("This is a test file.\n")
    f.write("Hello, World!\n")