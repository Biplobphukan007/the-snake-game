from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #turns off the tracer
snake = []
k = 0
for i in range(0, 3):
    new_turtle = Turtle()
    new_turtle.color("white")
    new_turtle.shape("square")
    new_turtle.penup()
    new_turtle.setx(-20*i)
    snake.append(new_turtle)



game_is_on = True
while game_is_on:
    #screen.update only when all the segments have moved forward
    screen.update()
    time.sleep(0.1)
    # for seg in snake:
    #     seg.forward(20)
    #making previous part of snake move into the forward part
    for seg_num in range(len(snake)-1, 0, -1):
        new_x = snake[seg_num-1].xcor()
        new_y = snake[seg_num-1].ycor()
        snake[seg_num].goto(new_x, new_y)
    snake[0].forward(20)
    snake[0].left(90)

screen.exitonclick()
