from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()

    def car(self):
        self.shape('square')
        self.color('red')
        self.shapesize(stretch_wid=1, stretch_len=2)

    def generate_car(self):
        for i in range(10):
            y_val = random.randint(-250, 250)
            self.goto(250, y_val)
            self.car()
            print('car called')




