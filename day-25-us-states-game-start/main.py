import turtle
from turtle import Screen, Turtle
import pandas
screen=Screen()
usmap=Turtle()
image="blank_states_img.gif"
screen.addshape(image)
usmap.shape(image)



# def load_the_components(x,y):
#     print(x,y)



# screen.onscreenclick(load_the_components)


# print(guess)
#TODO:5 - record the correct guesses in a list
list_of_correct_guesses=[]

states=pandas.read_csv("50_states.csv")
# print(type(states))
list_of_states=states["state"].to_list()
#TODO:4 - use a loop to allow users to keep guessing
game_is_on=True
while game_is_on:
    # TODO:6 - Keep track of the score
    user_input = screen.textinput(f"score: {len(list_of_correct_guesses)}/50 Do you know all the states in US ?", "type the state name")

    # TODO:1 - convert the guess to title case
    guess = user_input.title()
    if guess=="Exit":
        break
    # TODO:2 - check if the guess is among 50 states
    if guess in list_of_states:
        # print(guess + " is present")
        if guess  not in list_of_correct_guesses:
            list_of_correct_guesses.append(guess)
        x=states[states.state==guess]["x"].iloc[0]
        # print(x.iloc[0])
        y=states[states.state==guess]["y"].iloc[0]
        state_turtle=Turtle()
        state_turtle.hideturtle()
        state_turtle.up()
        # TODO:3 - write correct guesses on to map
        state_turtle.goto(x,y)
        state_turtle.write(f"{guess}",align="center",font=("Arial",8,"normal"))


    if len(list_of_correct_guesses)==50:
        game_is_on=False
        print("you have guessd all the states, congrats")


 # TODO:7 - states_to_learn.csv
if len(list_of_correct_guesses)<50:
    list_to_learn=list_of_states
    # with open("states_to_learn.csv","w") as learn:
    #     for state in list_of_correct_guesses:
    #         list_to_learn.remove(state)
    #     for item in list_to_learn:
    #         learn.write(item + "\n")
    for state in list_of_correct_guesses:
        list_to_learn.remove(state)
    list_to_learn_dataframe=pandas.DataFrame(list_to_learn)
    list_to_learn_dataframe.to_csv("list_of_states_to_learn.csv")





# screen.mainloop()