import turtle
from turtle import Screen, Turtle

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
#TODO:2 - check if the guess is among 50 states
#TODO:3 - write correct guesses on to map
#TODO:4 - use a loop to allow users to keep guessing
#TODO:5 - record the correct guesses in a list
#TODO:6 - Keep track of the score




screen.mainloop()