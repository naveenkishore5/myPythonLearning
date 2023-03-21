from turtle import Turtle, Screen
import random

first = Turtle()
screen = Screen()

is_race_on = False
screen.setup(width= 500, height=400)
user_bet = screen.textinput(title=  'Make your bet', prompt='which turtle will win the race? Enter a color: ')
print(user_bet)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
turtle_list = []

for i in range(6):
    turtle_new = Turtle(shape="turtle")
    turtle_new.penup()
    turtle_new.color(colors[i])
    turtle_new.goto(x=-230, y=y_position[i])
    turtle_list.append(turtle_new)

if user_bet:
    is_race_on = True

while is_race_on:
    for eachTurtle in turtle_list:
        if eachTurtle.xcor() > 230:
            is_race_on = False
            winning_color = eachTurtle.pencolor()
            if winning_color == user_bet:
                print(f'Congratulations, your turtle {winning_color} won this bet....')
            else:
                print(f'Better luck next time, turtle {winning_color} won this bet....')
        eachTurtle.forward(random.randint(0,10))





screen.exitonclick()