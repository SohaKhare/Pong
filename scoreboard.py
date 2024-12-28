
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,240)
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.l_score}    {self.r_score}", align=ALIGNMENT, font=FONT)

    def rightincrease(self):
        self.r_score += 1
        self.update()
    
    def leftincrease(self):
        self.l_score += 1
        self.update()


    