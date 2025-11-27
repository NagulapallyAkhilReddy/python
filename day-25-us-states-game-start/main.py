import turtle
from turtle import Screen, Turtle

screen=Screen()
usmap=Turtle()
image="blank_states_img.gif"
screen.addshape(image)
usmap.shape(image)



def load_the_components(x,y):
    print(x,y)

user_input=screen.textinput("Do you know all the states in US ?","type the state name")
# if user_input in

screen.onscreenclick(load_the_components)
screen.mainloop()