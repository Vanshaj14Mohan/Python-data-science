from turtle import *
s = Screen()
pensize(5)
speed("normal")
s.setup(400,400)
s.bgcolor("black")

pencolor("yellow")
for i in range(5):
    lt(72)
    for i in range(5):
        fd(150)
        rt(144)
mainloop()