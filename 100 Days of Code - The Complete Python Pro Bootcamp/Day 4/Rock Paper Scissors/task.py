import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,scissors,paper]
choice=int(input("choose your choice, 0 for rock, 1 for scissors,2 for paper"))
# if choice==0:
#     print(rock)
# elif choice==1:
#     print(scissors)
# elif choice==2:
#     print(paper)
# else:
#     print("please select a valid choice")
if 0<=choice<=2:
    print(game_images[choice])



computer_choice=random.randint(0,2)
# if computer_choice==0:
#     print(rock)
# elif computer_choice==1:
#     print(scissors)
# else:
#     print(paper)
print("computer choose:\n")
print(game_images[computer_choice])

if choice<0 or choice>2:
    print("you choose invalid option, you lose, i win ")
elif computer_choice==choice:
    print('it\'s a draw match,"play again"')
elif choice==0 and computer_choice==1 or choice==1 and computer_choice==2 or choice==2 and computer_choice==0:
    print("you win!!!")
else:
    print("ha ha ha, I beat you!")
