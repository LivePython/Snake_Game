import time
from turtle import Screen
from snake import Snake
from make_food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.title('Best Snake Game')
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)

snake = Snake()
food = Food()
score_count = ScoreBoard()

screen.listen()
screen.onkey(key='Up', fun=snake.up_fun)
screen.onkey(key="Down", fun=snake.down_fun)
screen.onkey(key='Left', fun=snake.left_fun)
screen.onkey(key="Right", fun=snake.right_fun)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # check collision with food
    if snake.head.distance(food) < 10:
        food.refresh_food()
        score_count.increase_score()
        snake.extend()

    # Check collision with the wall
    if snake.head.xcor() > 290 or \
            snake.head.ycor() > 290 or \
            snake.head.xcor() < -290 or \
            snake.head.ycor() < -290:
        game_on = False
        score_count.game_over()

    # Detect collision with the tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score_count.game_over()















screen.exitonclick()