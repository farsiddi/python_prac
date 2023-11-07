import turtle as tut
import random

# sq = tut.Turtle()
# tr = tut.Turtle()
# pg = tut.Turtle()
# hg = tut.Turtle()
#
# for i in range(4):
#     sq.forward(80)
#     sq.left(90)
#
# for i in range(3):
#     tr.forward(80)
#     tr.left(120)
#
# for i in range(5):
#     pg.forward(100)
#     pg.left(72)
#
# for i in range(6):
#     hg.forward(100)
#     hg.left(60)


sam = tut.Turtle()
sam_colour = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
              "SeaGreen"]


def drawing_shape():
    for no_side in range(3, 9):
        dist = 80
        ang = int(360 / no_side)
        sam.color(random.choice(sam_colour))
        for i in range(no_side):
            sam.forward(dist)
            sam.left(ang)


drawing_shape()

scr = tut.Screen()
scr.exitonclick()
