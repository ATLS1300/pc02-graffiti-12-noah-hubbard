#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

Turtle()

shape("turtle")

width(10)

color("forest green")

up()

goto(-200,100)

down()

begin_fill()

left(90)

forward(50)

left(90)

forward(50)

left(90)

forward(50)

left(90)

forward(50)

end_fill()

up()

goto(300,-200)

down()

color("royal blue")

circle(40)

up()

goto(300,100)

stamp()

goto(300,200)

shape("arrow")

width(3)

down()

right(45)

forward(50)

right(135)

forward(50)

right(135)

forward(50)

up()

goto(200,10)

shape("circle")

width(3)

down()

circle(175)

up()

goto(0,150)

color(173, 26, 132)

down()

dot(30)

up()

goto(100,150)

down()

dot(30)

up()

goto(-25,50)

down()

right(135)

width(5)

circle(80,180)







