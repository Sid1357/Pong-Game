from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(position)
    def display_left_score(self):
        self.write(f"{self.score}", font=("Arial", 30, "bold"))
    def display_right_score(self):
        self.write(f"{self.score}", font=("Arial", 30, "bold"))
    def update_left_score(self):
        self.score+=1
        self.clear()
        self.write(f"{self.score}", font=("Arial", 30, "bold"))
    def update_right_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", font=("Arial", 30, "bold"))