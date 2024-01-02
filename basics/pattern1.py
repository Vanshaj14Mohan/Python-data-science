from turtle import *  #turtle--> library

pensize(5) #size of pen
pencolor("violet")
speed("normal")

for i in range(6):  #range--> generator function, generates a sequence inside memory(0,1,2,3,4,5) 
    fd(120) # move forward 120 pixel
    lt(360/6) #turn at 360/6 => 60 degrees
    circle(60, steps=6) #create a circle of 60 radius 
    write(i+1) #i+ in the program
    #for j in range(6):
       #fd(60)
    #lt(360/6)

hideturtle()
mainloop()