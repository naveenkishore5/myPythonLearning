from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
turtle = Turtle()
screen.title('US State Quiz')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

us_states = pd.read_csv('50_states.csv')

us_states['state'] = us_states['state'].apply(str.lower)

allstate = us_states.state.tolist()


count = 0

while count < 50:
    name = screen.textinput(title=f'{count}/ 50 States Correct ', prompt="What's the state name? ")
    tur = Turtle()
    tur.hideturtle()
    tur.penup()
    states = us_states[us_states.state == name]
    tur.goto(int(states.x), int(states.y))
    tur.write(name)
    count += 1








# def get_coordinates(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_coordinates)
# turtle.mainloop()

screen.exitonclick()
