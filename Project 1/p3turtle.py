import turtle
t = turtle.Turtle()
#The background
turtle.screensize(canvwidth=600,canvheight=600, bg="green")
#The body of duck
from dt import *
t.fillcolor("yellow")
t.begin_fill()
drawTriangle(t,75)
t.end_fill()
#The head of duck
from dp import *
t.penup()
t.goto(-25,25)
t.pendown()
t.begin_fill()
drawCircle(t,25)
t.end_fill()
#The beak of duck
t.penup()
t.setposition(-50,0)
t.right(180)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.forward(30)
t.left(165)
t.forward(33)
t.end_fill()
#The eyeball of duck
t.penup()
t.setposition(-35,18)
t.left(15)
t.pendown()
t.fillcolor("white")
t.begin_fill()
drawCircle(t,8)
t.end_fill()
#The pupil of duck
t.penup()
t.setposition(-37,15)
t.pendown()
t.fillcolor("black")
t.begin_fill()
drawCircle(t,4)
t.end_fill()
#The wing of duck
t.penup()
t.setposition(25,-10)
t.pendown()
drawTriangle(t,30)
#The feet of duck
from do import *
t.penup()
t.setposition(9,-50)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
drawOval(t,10)  #foot number 1
t.end_fill()
t.penup()
t.setposition(14,-60)
t.pendown()
t.begin_fill()
drawOval(t,10)  #foot number 2
t.end_fill()

#voila! the duck is complete



