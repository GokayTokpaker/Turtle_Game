import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
FONT = ('Arial', 20, 'normal')
score = 0
# score turtle
score_turtle = turtle.Turtle()
#countdown turtle
countdown_turtle = turtle.Turtle()
# list of turtle
tuList = []
game_over = False
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2  # positive height/2 is the top of the screen
    y = top_height * 0.9  # decreasing a bit so text will be visible
    score_turtle.setposition(0, y)
    score_turtle.write(arg='Score:0', move=False, align='center', font=FONT)
grip_size = 10
def make_turtle(x,y):
    def click_turtle(x,y):
        global score
        score +=1
        score_turtle.clear()
        score_turtle.write(arg=f'Score: {score}', move=False, align='center', font=FONT)
        print(x,y)
    t = turtle.Turtle()
    t.onclick(click_turtle)
    t.color("blue")
    t.shapesize(1.5,1.5)
    t.penup()
    t.goto(x*grip_size,y*grip_size)
    t.shape("turtle")
    tuList.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10]
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtle():
    for i in tuList:
        i.hideturtle()
#recursive function
def show_turtle_randomly():
    if not game_over:
        hide_turtle()
        random.choice(tuList).showturtle()
        screen.ontimer(show_turtle_randomly, 1000)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("red")
    countdown_turtle.penup()

    top_height = screen.window_height() / 2  # positive height/2 is the top of the screen
    y = top_height * 0.9  # decreasing a bit so text will be visible
    countdown_turtle.setposition(0, y-30)
    if time>0:
        countdown_turtle.clear()
        countdown_turtle.write(arg='Score:{}'.format(time), move=False, align='center', font=FONT)
        screen.ontimer(lambda:countdown(time-1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtle()
        countdown_turtle.write(arg='GAME OVER!!!', move=False, align='center', font=FONT)

def game_start():
    turtle.tracer(0)
    setup_score_turtle()
    countdown(10)
    setup_turtles()
    hide_turtle()
    show_turtle_randomly()
    turtle.tracer(1)

game_start()
turtle.mainloop()