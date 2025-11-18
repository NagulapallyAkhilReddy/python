import random
from random import sample
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def wanna_play():
    play_or_no=input("Do you want to play a game of BLACK JACK? type 'y' or 'n' : ")
    if play_or_no=='y':
        print(art.logo)
        player_cards=random.sample(cards,2)
        print(f"your cards: {player_cards},  current score:{sum(player_cards)}")
        computer_cards = random.sample(cards, 2)
        print(f"computer's first card:{computer_cards[0]}")


        if sum(player_cards)==21:
            print("Black Jack, you win!!")
            wanna_play()
        else:
            hit_or_pass = input("type 'y' to get another card, or 'n' to pass : ")
            while hit_or_pass == 'y':
                player_cards.append(random.choice(cards))
                if sum(player_cards)>21:
                    if 11 in player_cards:
                        ind=player_cards.index(11)
                        player_cards[ind]=1
                    else:
                        print(f"you busted! you went over 21 your total score is {sum(player_cards)}")
                        wanna_play()
                print(f"your cards: {player_cards}, current score:{sum(player_cards)}")
                print(f"computer's first card:{computer_cards}")

                hit_or_pass = input("type 'y' to get another card, or 'n' to pass : ")
            if hit_or_pass=='n':
                if sum(computer_cards)==21:
                    print("chitti the robo won blackjack!!")
                    print(f"computer final cards{computer_cards}")
                    wanna_play()
                while sum(computer_cards)<17:
                    computer_cards.append(random.choice(cards))
                while sum(computer_cards)>21:
                    if 11 in computer_cards:
                        ind=computer_cards.index(11)
                        computer_cards[ind]=1
                    else:
                        print("computer busted!!, you won")
                        print(f"your final cards {player_cards}\n computer final cards {computer_cards}")
                        wanna_play()
                while sum(computer_cards)<17:
                    computer_cards.append(random.choice(cards))
                if sum(computer_cards)>17:
                    y=21-sum(computer_cards)
                    x=21-sum(player_cards)
                    if x<y:
                        print(f"you win, your total is {sum(player_cards)}, and computer score is {sum(computer_cards)}")
                        print(f"your final cards {player_cards}\n computer final cards {computer_cards} ")
                        wanna_play()
                    elif x==y:
                        print(f"it's a draw, you both have {sum(player_cards)} in total")
                        print(f"your final cards {player_cards}\n computer final cards {computer_cards} ")

                        wanna_play()
                    elif x>y:
                        print(f"you lose, your total is {sum(player_cards)}, and computer score is {sum(computer_cards)}")
                        print(f"your final cards {player_cards}\n computer final cards {computer_cards} ")

                        wanna_play()




    else:
        print("have a good day! bye")
wanna_play()