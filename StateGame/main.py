import turtle as tut

sc = tut.Screen()
sc.title("Welcome to the India State Game")
# sc.bgpic("blank_states_img.gif")  # Turtles works with gif only
image = "India-state.gif"
# sc.setup(height=865, width=800)
sc.addshape(image)
tut.shape(image)

user_guess = tut.textinput("Make you guess", "What,s the another state name ?").title()
print(user_guess)
# Getting the x and y coordinate
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
# tut.onscreenclick(get_mouse_click_coordinate)


tut.mainloop()
