# # import turtle
# import another_module
#
# from turtle import Turtle,Screen
#
# print(another_module.another_variable)
#
# jhonny=Turtle()
# print(jhonny)
# jhonny.color("orange")
# jhonny.shape("turtle")
# jhonny.up()
# jhonny.forward(100)
# print(jhonny.position())
# jhonny.backward(200)
#
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"],"l")
table.add_column("Type",["Electric","Water","Fire"],"l")
table.align="r"
print(table)
