from turtle import Turtle
START_POSITION = [(-20, 0), (-10, 0), (0, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):

        self.segment = []
        self.snake()
        self.MOVE_DISTANCE = 20

    def snake(self):
        for position in START_POSITION:
            s = Turtle(shape='square')
            s.shapesize()
            s.color('black')
            s.penup()
            s.goto(position)
            self.segment.append(s)
            self.head = self.segment[0]

    def move(self):
        for seg_num in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg_num-1].xcor()
            new_y = self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x, new_y)

        self.head.forward(self.MOVE_DISTANCE)

    def create_snake(self):
        for position in START_POSITION:
            self.add_segement(position)

    def add_segement(self, position):
        s = Turtle(shape='square')
        s.shapesize()
        s.color('white')
        s.penup()
        s.goto(position)
        self.segment.append(s)

    def extend(self):
        self.add_segement(self.segment[-1].position())

    def up_fun(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down_fun(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right_fun(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def left_fun(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(LEFT)


