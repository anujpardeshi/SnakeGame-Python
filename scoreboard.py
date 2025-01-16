from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 26, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score : {self.high_score}", align= "center", font=("Arial", 22, "normal"))

    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align= ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
            
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align= ALIGNMENT, font=FONT)
