import random
import sys
import os

#creating a test file to lear some file Input output

test_file = open("test.txt","wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("write me to the file\n", 'UTF-8'))
test_file.close()
test_file =open("test.txt","rt")
text_in_file = text_file.read()
print(text_in_file)

os.replace(test.txt)

