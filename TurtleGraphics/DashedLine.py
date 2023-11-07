import turtle as tut

sam = tut.Turtle()
sam.shape("turtle")

# sam.forward(15)
# sam.penup()
# sam.forward(15)
# sam.pendown()
# sam.forward(15)

for i in range(16):
    sam.forward(15)
    sam.penup()
    sam.forward(15)
    sam.pendown()
    sam.left(22.5)





jam = tut.Screen()
jam.exitonclick()