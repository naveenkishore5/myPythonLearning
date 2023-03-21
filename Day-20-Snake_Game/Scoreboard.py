from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.max_score = self.get_maxscore()
        self.color('White')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def get_maxscore(self):
        with open('data.txt', 'r') as f:
            return int(f.read())

    def update_maxscore(self):
        with open('data.txt', 'w') as f:
            f.write(str(self.max_score))



    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.count}  High Score: {self.max_score}', align = ALIGNMENT, font = FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.count > self.max_score:
            self.max_score = self.count
        self.count = 0
        self.update_scoreboard()

    def increase_score(self):
        self.count += 1
        self.update_scoreboard()



