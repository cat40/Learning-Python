# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 07:21:17 2016

@author: Backup
"""

p = (180-135) 
i = (100)

import turtle
turtle.RawPen(turtle.Screen())
turtle.color("red", "blue")
turtle.pu()
turtle.setpos(-i/2, i+ 20)
turtle.pd()

turtle.fill(True)
for b in range(0,8,1):
    turtle.fd(i)
    turtle.right(p)
    
turtle.fill(False)

turtle.pu()
turtle.setpos(-70,20)
turtle.right(p-45)
turtle.pd()
turtle.write("Timmy is a Teacher now", True, "left",("Times New Roman", 12, "normal"))

import time
time.sleep(10)

import IPython
app = IPython.Application.instance()
app.kernel.do_shutdown(True)  