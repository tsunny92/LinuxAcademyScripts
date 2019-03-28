#!/usr/bin/env python3.6

file1 = open("testing.txt", 'a+')
file1.write("Appending contents\n")

# After appending pointer moves to last position
# If again that same file needs to be read then set the pointer to 0

file1.seek(0)
print(file1.read())
file1.close()

# For writing and reading file

file2 = open("testfle", 'w+')
file2.write("Creating and writing to new file\n")
file2.seek(0)
print(file2.read())
file2.close()

# Using with it can automatically close file operations 

with open("testfle",'a+') as f:
    f.write("Adding contents to new file\n")
    f.seek(0)
    print(f.read())

