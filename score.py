from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.updatescore()
    
    
    def scoreboard(self):
        self.score = self.score + 1
        self.clear()
        self.updatescore()
        
    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Arial",22,"normal"))
        self.home()
        
    def updatescore(self):
        self.write(f"Score: {self.score}",align="center",font=("Arial",22,"normal"))
        