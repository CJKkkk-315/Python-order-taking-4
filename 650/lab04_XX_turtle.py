# siyu yin
# csce 101-002
# 2023.02.09
# ysiyu@email.sc.edu
# Lab1
import turtle
t = turtle.Turtle()
colors = ['red','green','blue']
turtle.bgcolor('pink')
t.screen.setworldcoordinates(0,0,13,13)
t.pensize(10)
t.penup()
t.goto(0,12)
t.pendown()
for i in range(12):
    t.pencolor(colors[i%3])
    t.fd(12-i-1)
    t.penup()
    t.goto(0,12-i-1)
    t.pendown()