import  turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        # self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]#made this as constant
        self.my_snake = []
        self.create_snake()
        # for position in self.starting_positions:
        #     my_snake_part = turtle.Turtle("square")
        #     my_snake_part.color("white")
        #     my_snake_part.shape("square")
        #     my_snake_part.up()
        #     my_snake_part.setposition(position)
        #
        #     self.my_snake.append(my_snake_part)#moved this into seperate method

    def create_snake(self):

        for position in STARTING_POSITIONS:
            my_snake_part = turtle.Turtle("square")
            my_snake_part.color("white")
            my_snake_part.shape("square")
            my_snake_part.up()
            my_snake_part.setposition(position)
            self.my_snake.append(my_snake_part)

    def move(self):

        for index in range(len(self.my_snake) - 1, 0, -1):
            x = self.my_snake[index - 1].xcor()
            y = self.my_snake[index - 1].ycor()
            self.my_snake[index].goto(x, y)

        self.my_snake[0].left(90)
        self.my_snake[0].forward(20)