import turtle
from turtle import Screen

def move_forward():
    etchy.forward(10)

def move_backward():
    etchy.backward(10)

def move_clockwise():
    etchy.right(10)

def move_counter_clockwise():
    etchy.left(10)

def clear_sketch():
    etchy.clear()
    etchy.up()#after mam's explanation added these lines
    etchy.home()
    etchy.down()
etchy=turtle.Turtle()
sketch_screen=Screen()

sketch_screen.listen()
sketch_screen.onkey(key="w",fun=move_forward)
sketch_screen.onkey(key="s",fun=move_backward)
sketch_screen.onkey(key="a",fun=move_counter_clockwise)
sketch_screen.onkey(key="d",fun=move_clockwise)
sketch_screen.onkey(key="c",fun=clear_sketch)
sketch_screen.exitonclick()