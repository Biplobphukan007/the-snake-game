from turtle import Turtle
FONT = ("Courier New", 15, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", move = False, align = 
    'left', font = FONT)
        self.hideturtle()
    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER", align = "left", font = FONT)

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move = False, align = 
    'left', font = FONT)
        # self.goto(0, 280)
        