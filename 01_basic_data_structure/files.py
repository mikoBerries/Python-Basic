import os

# get PWD
print(os.getcwd()+"\myfile.txt")

f=open(os.getcwd()+"\myfile.txt")
print(f.read())

# reset reader cursor
f.seek(0)
print()

# get one lines from reader
print(f.readline())
f.seek(0)
# getting all lines separated i list
print(f.readlines())
f.close

# https://www.geeksforgeeks.org/with-statement-in-python/
#  setting mode read / write /creating/etc
with open(os.getcwd()+"\myfile.txt" ,mode="r") as file:
    filedata = file.read()

print(filedata)