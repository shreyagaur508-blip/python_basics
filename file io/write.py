#writing to a file
f = open("sample.txt", "w")
f.write("Hello, World!\n")
f.write("This is a test file.\n")
f.close()


#reading from the fil
f = open("sample.txt", "r")
content = f.read()
print(content)
f.close()