# robo1.py

import turtle

t=turtle.Pen()
for x in range(1,100):
    t.forward(x)
    t.left(90)
    if x % 50 == 0:
        t.forward(x)
        t.right(90)