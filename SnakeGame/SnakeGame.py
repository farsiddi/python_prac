import time
import turtle as tut
from snake import Snake

sc = tut.Screen()
sc.setup(height=600, width=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)
snake_cor = [(0, 0), (-20, 0), (-40, 0)]
snake_segment = []

snake = Snake()
sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_on = True

while game_on:
    sc.update()
    time.sleep(0.1)
    # for seg in snake_segment:
    #     seg.forward(20)
    snake.snake_move()

sc.exitonclick()
