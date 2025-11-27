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

user_input=screen.textinput("Do you know all the states in US ?","type the state name")

#TODO:1 - convert the guess to title case
guess=user_input.title()
# print(guess)
#TODO:2 - check if the guess is among 50 states
states=pandas.read_csv("50_states.csv")
# print(type(states))
list_of_states=states["state"].to_list()

if guess in list_of_states:
    print(guess + " is present")
#TODO:3 - write correct guesses on to map
#TODO:4 - use a loop to allow users to keep guessing
#TODO:5 - record the correct guesses in a list
#TODO:6 - Keep track of the score




screen.mainloop()