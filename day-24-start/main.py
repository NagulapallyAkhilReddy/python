# file=open("my_file.txt")
# contents=file.read()
# print(contents)
#file.close()#we can use 'with' to automatically close it
from importlib.resources import contents

# file.write("Hi there")#error not writable
# contents=file.read()
# print(contents)

with open("my_file.txt",mode="a") as file:
    # content=file.read()
    # print(content)
    file.write("\nit is simple")

with open("my_file.txt") as file:
    content=file.read()
    print(content)
