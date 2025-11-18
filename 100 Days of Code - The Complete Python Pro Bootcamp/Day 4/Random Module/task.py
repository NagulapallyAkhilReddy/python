import random
import my_module
# num=int(random.random()*10)
print(my_module.my_fav_num)
# if num%2==0:
#     print("heads")
# else:
#     print("tails")
random_num=int(random.random()*10)
print(random_num)

random_num1=random.uniform(1,10)
print(random_num1)
if random_num%2==0:
    print("heads")
else:
    print("tails")


random_heads_or_tails=random.randint(0,1)
if random_heads_or_tails==0:
    print("heads")
else:
    print("tails")

