import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    if n1>n2:
        return n1-n2
    else:
        return n2-n1

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
# print(operations["*"](4,8))
continue_or_not="yes"
n1=int(input("what's the first number?:"))

while continue_or_not=="yes":

    for key in operations:
        print(key)
    operation=input("pick an operation: ")
    n2=int(input("what's the next number?: "))
    result=operations[operation](n1,n2)
    print(f"{n1} {operation} {n2} = {result}")
    continue_cal=input(f"type 'y' to continue calculating with {result}, or type n to start new calculation , and to stop type s")
    if continue_cal=='y':
        n1=result
    elif continue_cal=='n':
        n1 = int(input("what's the first number?:"))
    elif continue_cal=='s':
        continue_or_not="no"




