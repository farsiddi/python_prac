import turtle
import turtle as tut
import random

sam = tut.Turtle()
turtle.colormode(255)


# sam_colour = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#               "SeaGreen"]
def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direct = [0, 90, 180, 270]
sam.pensize(10)
sam.speed("fast")
for i in range(80):
    sam.forward(30)
    sam.setheading(random.choice(direct))
    sam.color(rand_color())

sc = tut.Screen()
sc.exitonclick()
