from turtle import Screen, Turtle, color
from random import randint, choice
import colorgram
test = Turtle()
test.shape('turtle')
test.color('red')
# test.pensize(15)
# test.speed('fastest')
# colours = ["red", "green", "black", "blue", "yellow", "dark magenta", "dark slate gray", "dodger blue"]
# walk = [0, 90, 180, 270]
# for i in range(200):
#     test.pencolor(choice(colours))
#     test.forward(30)
#     test.setheading(choice(walk))

test.speed('fastest')
test.circle(50)
for i in range(50):
    test.circle(50)
    curr = test.heading()
    test.setheading(curr + 10)



screen = Screen()
screen.exitonclick()
