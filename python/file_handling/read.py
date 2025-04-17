#!/bin/python3

f = open("test.txt", "r")

# reads whole file (you can also specify the total charas to output)
# file_content = f.read()
# print(file_content)

# read line by line
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")

f.close()