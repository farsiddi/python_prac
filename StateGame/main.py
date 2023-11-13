import turtle as tut
import pandas

data = pandas.read_csv("states_data.csv")
state_name = data.state.to_list()
print(state_name)

sc = tut.Screen()
sc.title("Welcome to the India State Game")
image = "India-state.gif"  # Turtles works with gif only
# sc.setup(height=865, width=800)
sc.addshape(image)
tut.shape(image)
guess_state = []

while len(guess_state) < 29:
    user_guess = tut.textinput(f"{len(guess_state)}/29 state guessed",
                               'What,s the another state name? or type "Exit" to exit the game').title()
    if user_guess == "Exit":  # Ends the game
        missing_state = [state for state in state_name if state not in guess_state]
        # Above line is same as working below commented lines
        # missing_state = []
        # for state in state_name:
        #     if state not in guess_state:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("MissingState.csv")
        # print(missing_state)
        break
    if user_guess in state_name:
        guess_state.append(user_guess)
        sam = tut.Turtle()
        sam.hideturtle()
        sam.penup()
        state_data = data[data.state == user_guess]
        sam.goto(int(state_data.x), int(state_data.y))
        sam.write(user_guess)
        # sam.write(state_data.state.item())

# Getting the x and y coordinates  => Used to get the x and y coordinate of mouse click
# te
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
# tut.onscreenclick(get_mouse_click_coordinate)

# tut.mainloop()
