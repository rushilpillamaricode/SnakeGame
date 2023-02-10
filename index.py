from snake import Snake
from food import Food
from turtle import Screen
from score import Score
import time

screen = Screen();
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
screen = Screen()
score = Score()

loop = True
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while loop:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.growth()
        score.scoreboard()  

    x = snake.segments[0].xcor()
    y = snake.segments[0].ycor()
    if(x > 280 or x < -280 or y > 280 or y < -280):
        loop = False
        score.gameover()
    
    
    for segment in snake.segments:
        if(segment == snake.segments[0]):
            pass
        else:
            if(snake.segments[0].distance(segment) < 10):
                loop = False
                score.gameover()
                break
                


screen.exitonclick()