from turtle import Screen, Turtle

pong_screen=Screen()
pong_screen.setup(800,500)
pong_screen.bgcolor("black")
pong_screen.tracer(0)
x=0
y=228
i=0
# pong_dash=[]
while y>-250:
    pong_dash_single=Turtle()
    pong_dash_single.color("white")
    pong_dash_single.shape("square")
    pong_dash_single.shapesize(1,0.2)
    # pong_dash[i].speed("slow")
    pong_dash_single.up()

    pong_dash_single.setposition(x,y)
    y = y - 30
    # pong_dash.append(pong_dash_single)
    i+=1

pong_screen.update()


pong_screen.exitonclick()