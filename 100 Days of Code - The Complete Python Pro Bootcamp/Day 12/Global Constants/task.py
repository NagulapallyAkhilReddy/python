PI=3.14
URL="https://google.com"

def my_function():
    global PI
    PI+=PI
    print(PI)
    print(URL)



print(PI)
print(URL)

my_function()