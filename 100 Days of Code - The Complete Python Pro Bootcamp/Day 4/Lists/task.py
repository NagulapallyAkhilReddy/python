import random

friends = ["at home", "at school", "at intermediate", "at btech", "at masters"]

print(friends[random.randint(0, 4)])
friends.append("at job")
friends.extend(("at parties", "at events" ,"at functions"))
print(friends)


