import  turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        # self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]#made this as constant
        self.my_snake = []
        self.create_snake()
        self.head=self.my_snake[0]#after ma's explanation
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

        # self.my_snake[0].left(90)
        self.head.forward(MOVE)#made as constant

    def up(self):
        # print(self.my_snake[0].mode())
        if self.my_snake[0].heading()==DOWN:
            pass
        else:
            self.my_snake[0].setheading(UP)


        # print(self.my_snake[0].heading())

    def down(self):
        if self.my_snake[0].heading() == UP:
            pass
        else:
            self.my_snake[0].setheading(DOWN)
        # print(self.my_snake[0].heading())


    def right(self):
        if self.my_snake[0].heading() == LEFT:
            pass
        else:
            self.my_snake[0].setheading(RIGHT)
        # print(self.my_snake[0].heading())

    def left(self):
        if self.my_snake[0].heading() == RIGHT:
            pass
        else:
            self.my_snake[0].setheading(LEFT)
        # print(self.my_snake[0].heading())
