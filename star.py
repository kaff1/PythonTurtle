import colorsys
import turtle

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)

n = 70
h = 0
while True:
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.color(c)
    t.forward(1000)
    t.left(170)
