class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0
        print("new user being created...")

    def follow(self,user):
        user.followers+=1
        self.following+=1




user_1=User("001","akhil")
# user_1.id="001"
# user_1.username="akhil"

print(user_1.username)
print(user_1.followers)

user_2=User("007","kittu")
# user_2.id="007"
# user_2.username="kittu"
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.following)
print(user_2.followers)