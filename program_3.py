import turtle as tk
t=tk.Turtle()
t.color('white')
t.speed(1)          #control speed of pen
wn=tk.Screen()
wn.bgcolor('black')
t.begin_fill()
t.fillcolor('blue')
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()
t.hideturtle()      #hide turtle
tk.exitonclick()    #hold output screen