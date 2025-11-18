import random

import art
import game_data
#mam did it in more organized and better way, gotta check it out in solution.py
length=len(game_data.data)
index_list=[]
for i in range(0,50):
    index_list.append(i)



def pick_index():
    return random.choice(index_list)


compare_index=pick_index()
against_index=pick_index()
store_index=0
score=0

def start_game():
    global against_index
    against_index = pick_index()


print(art.logo)
condition=True

while condition:

    if compare_index!=against_index:

        print(
            f"Compare A: {game_data.data[compare_index]['name']},{game_data.data[compare_index]['description']}, from {game_data.data[compare_index]['country']}")
        print(art.vs)
        print(
            f"against B: {game_data.data[against_index]['name']},{game_data.data[against_index]['description']}, from {game_data.data[against_index]['country']}")
        higher_or_lower=input("Who has more followers? type 'A' or 'B'")
        print("\n"*20)
        if higher_or_lower.lower()=='a':
            if game_data.data[compare_index]['follower_count']>game_data.data[against_index]['follower_count']:
                store_index=against_index
                against_index=pick_index()
                score+=1
                compare_index=store_index
                print(art.logo)
                print(f"you got it right, your current score is :{score} ")

            else:
                condition=False
                print(art.logo)
                print(f"sorry you lost,your final score is {score} ")
        elif higher_or_lower.lower()=='b':
            if game_data.data[compare_index]['follower_count']<game_data.data[against_index]['follower_count']:
                store_index=against_index
                against_index=pick_index()
                score+=1
                compare_index=store_index
                print(art.logo)
                print(f"you got it right, your current score is :{score} ")
            else:
                condition=False
                print(art.logo)
                print(f"sorry you lost,your final score is {score} ")

    else:
        start_game()