# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 17:45:03 2016

@author: Backup
"""
import math

import turtle
turtle.RawPen(turtle.Screen())

p = (math.pi*3/4) 
i = 400

turtle.radians()
turtle.pu()
turtle.setpos(-i/2, (i*5/24) + 20)
turtle.pd()
turtle.color("red", "blue")

turtle.fill(True)
for b in range(0,8,1):
    turtle.fd(i)
    turtle.right(p)

turtle.fill(False)

turtle.pu()
turtle.setpos(-70,20)
turtle.left(p*8/3)
turtle.pd()
turtle.write("Timmy is a Teacher now", True, "left",("Times New Roman", 12, "normal"))

import time
time.sleep(10)

import IPython
app = IPython.Application.instance()
app.kernel.do_shutdown(True)  