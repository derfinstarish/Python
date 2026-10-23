# create

# a = open("file.text", "x")
# print("Successfully created a file named file.text")

#write
# a = open("file.text", "w")
# print("Successfully opened file.text")

# #append
# a = open("file.text", "a")
# a.write("This is a test file.\n")
# a.close()
# print("Successfully appended to file.text")

# #read
# a = open("file.text", "r")
# print("Successfully opened file.text")
# print(a.read())
# a.close()

# # with statement
# with open("file.text", "w") as a:
#     a.write("This is a test file.\n")

# #delete
import os
os.remove("file.text")
print("File deleted.")