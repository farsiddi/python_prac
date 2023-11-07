import turtle
import random
from ExtractColorImage import color_list
import turtle as tut

turtle.colormode(255)
sam = tut.Turtle()
sam.speed("fastest")
sam.hideturtle()
sam.setheading(225)
sam.penup()
sam.forward(220)
# sam.pendown()
sam.setheading(0)
number_of_dots = 50

for no_dots in range(1, number_of_dots + 1):
    sam.dot(20, random.choice(color_list))
    sam.penup()
    sam.forward(50)
    # sam.pendown()
    if no_dots % 5 == 0:
        sam.setheading(90)
        sam.penup()
        sam.forward(50)
        sam.setheading(180)
        sam.forward(250)
        sam.setheading(0)

sc = tut.Screen()
sc.exitonclick()
