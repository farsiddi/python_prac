import turtle as tut
import random

turtle_color = ["red", "blue", "yellow", "green", "orange"]
race_on = False
sc = tut.Screen()
sc.setup(width=800, height=600)
usr_bet = sc.textinput("Make your bet", "Which color turtle will win")
turtle_list = []

y_axis = -20
for no_turtle in range(0, 5):
    new_turtle = tut.Turtle(shape="turtle")
    # new_turtle.speed("fast")
    new_turtle.color(turtle_color[no_turtle])
    new_turtle.penup()
    new_turtle.goto(-385, y_axis)
    y_axis += 40
    turtle_list.append(new_turtle)

if usr_bet:
    race_on = True

while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 360:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == usr_bet:
                print(f"You have won the race. Your winning color turtle is: {turtle.penup()}")
            else:
                print(f"You have lost. The winning color turtle is: {winning_color}")
        rand_dist = random.randint(0, 20)
        turtle.forward(rand_dist)

# print(usr_bet)
sc.exitonclick()
