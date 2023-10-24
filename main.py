import turtle
from turtle import Turtle,Screen
t1=Turtle()
scr = Screen()

def front():
    t1.forward(30)

def back():
    t1.backward(30)

def change_angle_right():
    t1.right(30)

def change_angle_left():
    t1.left(30)

def clr():
    t1.clear()
def circle():
    x=int(input("enter circle size"))
    t1.circle(x)

def reset():
    t1.home()
    t1.clear()

scr.listen()
scr.onkey(key="Up", fun= front)
scr.onkey(key="Down", fun= back)
scr.onkey(key="Right", fun= change_angle_right)
scr.onkey(key="Left", fun= change_angle_left)
scr.onkey(key="d",fun = clr)
scr.onkey(key="c",fun = circle)
scr.onkey(key="r",fun = reset)

scr.exitonclick()