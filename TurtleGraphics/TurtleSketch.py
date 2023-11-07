import turtle as tut

sam = tut.Turtle()


def move_fwd():
    sam.forward(30)


def move_bwd():
    sam.backward(30)


def move_left():
    new_heading = sam.heading() + 10
    sam.setheading(new_heading)


def move_right():
    new_heading = sam.heading() - 10
    sam.setheading(new_heading)


def clear_screen():
    sam.clear()
    sam.penup()
    sam.home()
    sam.pendown()


sc = tut.Screen()
sc.listen()
sc.onkey(move_fwd, "w")
sc.onkey(move_bwd, "s")
sc.onkey(move_left, "a")
sc.onkey(move_right, "d")
sc.onkey(clear_screen, "c")
sc.exitonclick()
