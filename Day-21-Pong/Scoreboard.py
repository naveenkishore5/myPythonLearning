from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('White')
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_scoreboard()
        self.create_center_line()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f'{self.lscore}', align= 'center', font= ('Arial', 24, 'normal'))
        self.goto(100, 250)
        self.write(f'{self.rscore}', align='center', font=('Arial', 24, 'normal'))

    def l_point(self):
        self.lscore += 1
        self.update_scoreboard()

    def r_point(self):
        self.rscore += 1
        self.update_scoreboard()


    def create_center_line(self):
        y = 300
        self.width(4)
        self.goto(0, 295)
        self.right(90)
        while y:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
            y -= 10










