from turtle import Turtle, Screen
import time
from snake import Snake
from food import food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height= 600, width=600)
screen.screensize(canvheight=320, canvwidth=320)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.head.xcor()> 300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()< -300:
        scoreboard.reset()
        snake.reset()


    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()
            
screen.exitonclick()
