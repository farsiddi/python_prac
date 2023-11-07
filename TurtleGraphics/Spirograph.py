import random
import turtle as tut

sam = tut.Turtle()
sam.speed("fastest")
tut.colormode(255)
sam.pensize(2)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spiral(size_gap):
    for i in range(int(360 / size_gap)):
        sam.color(random_color())
        sam.circle(75)
        curr_heading = sam.heading()
        sam.setheading(curr_heading + size_gap)


draw_spiral(5)
sc = tut.Screen()
sc.exitonclick()
