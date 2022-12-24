from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(0, 270)
        self.edit_score()

    def increase_score(self):
        self.undo()
        self.score += 1
        self.edit_score()

    def edit_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=('Arial', 20, 'normal'))
