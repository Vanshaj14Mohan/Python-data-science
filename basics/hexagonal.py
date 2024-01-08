from turtle import *
pensize(2)
bgcolor("black")
speed("fastest")
colors =["red", "purple", "green", "blue", "violet", "blue"] 
for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(60)
mainloop()