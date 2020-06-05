import turtle as tk
t=tk.Turtle()
tk.bgcolor('black')
l=['red','purple','blue','green','orange','yellow']
for i in range(360):
    t.pencolor(l[i%6])
    t.width(i/100+1)
    t.forward(i)
    t.left(59)
tk.exitonclick()