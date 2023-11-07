import turtle as tut

sam = tut.Turtle()
sc = tut.Screen()


def move_fwd():
    sam.forward(30)


sc.listen()
sc.onkey(key="space", fun=move_fwd)  # When we pass a function into another function we don't use parenthesis
sc.exitonclick()
