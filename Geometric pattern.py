from turtle import *
import random

#create a screen
screen = Screen()
screen.screensize(600,600,'black')

#create a pen to draw geometric pattern
pen = Pen()
pen.speed(150)

size = 20

for i in range(150):
    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,225)
    
    randcol = (r,g,b)

    colormode(255)

    pen.color(randcol)

    pen.circle(size,steps = 4)
    pen.right(55)

    size = size +3


