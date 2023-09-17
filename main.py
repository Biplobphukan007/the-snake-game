from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Score

#LEVEL CHANGE, increase the level value to make snake slower
level = 0.1

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(level)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_update()
        snake.extend()
    #Detect collision with wall
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() <= -290 or snake.head.ycor() >= 290:
        game_is_on = False
        score.game_over()
    #Detect collision with tail
    #if head collides with any segment
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()

