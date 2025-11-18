import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# #easylevel
password=""
if nr_letters<0:
    print("please give valid input for no of letters")
elif nr_letters>0:
    for n in range(0,nr_letters):
        p_letter=random.choice(letters)
        password+=p_letter
if nr_numbers<0:
    print("please give valid input for no of numbers")
elif nr_numbers>0:
    for n in range(0,nr_numbers):
        p_number=random.choice(numbers)
        password+=p_number
if nr_symbols<0:
    print("please give valid input for no of symbols")
elif nr_symbols>0:
    for n in range(0,nr_symbols):
        p_symbol=random.choice(symbols)
        password+=p_symbol
print(password)

#hard level
# list_password=password.split()
# passswordlength=nr_symbols+nr_numbers+nr_letters
# print(passswordlength)
# p=random.choice(password)
# password.remove(p)
final_password=""
password_as_list=list(password)
for n in password:

    choice_of=random.choice(password_as_list)
    password_as_list.remove(choice_of)
    final_password+=choice_of


print(final_password)












# password=""
# for num in range(1,nr_letters+1):
#     password+=random.choice(letters)
# for num in range(1,nr_numbers+1):
#     password+=random.choice(numbers)
# for num in range(1,nr_symbols+1):
#     password+=random.choice(symbols)
# print(password)
#
# # hardlevel
# passwordlist=[]
# for num in range(1,nr_letters+1):
#     passwordlist.append(random.choice(letters))
# for num in range(1,nr_numbers+1):
#     passwordlist.append(random.choice(numbers))
# for num in range(1,nr_symbols+1):
#     passwordlist.append(random.choice(symbols))
#
# hard_password=""
# for num in range(1,nr_symbols+nr_numbers+nr_letters+1):
#     hard_password+=random.choice(passwordlist)
# print(hard_password)

