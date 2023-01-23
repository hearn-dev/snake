from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as high_score:
            self.high_score = int(high_score.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def set_high_score(self, score):
        with open('high_score.txt', mode='w') as high_score:
            high_score.write(str(score))
            self.high_score = score

    def reset(self):
        if self.score > self.high_score:
            self.set_high_score(self.score)
        self.score = 0
        self.update_scoreboard()
