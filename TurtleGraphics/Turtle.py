import turtle

jack = turtle.Turtle()

jack.shape("turtle")
jack.color("red")


# jack.forward(100)
# jack.right(90)
# jack.forward(100)
# jack.right(90)
# jack.forward(100)
# jack.right(90)
# jack.forward(100)
# jack.right(90)

# def turtle_sq():
#     i = 0
#     while i < 4:
#         jack.forward(100)
#         jack.right(90)
#         i += 1
#
#
# turtle_sq()

for i in range(4):
    jack.forward(100)
    jack.right(90)

screen = turtle.Screen()
screen.exitonclick()
