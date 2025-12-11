print("Sinh vien: LE HOANG VU")
print("Ma so SV : 245751030110084")
print("#############################")
import turtle
import random

colors = ["red","green","blue","orange","purple","pink","yellow"]

t = turtle.Turtle()
t.pensize(3)

for i in range(12):
    t.pencolor(random.choice(colors))
    t.circle(100)
    t.right(30)

turtle.done()
