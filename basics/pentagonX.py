from turtle import *
speed("normal")
def pentagon(size, color):
    fillcolor(color)
    begin_fill()
    for i in range(5):
        fd(size)
        lt(360/5)
    end_fill()

#use
for i in range(6):
    pentagon(100, "red")
    pentagon(75, "blue")
    pentagon(45, "violet")
    fd(100)
    lt(360/6)
hideturtle()
mainloop()