import turtle as tk
t=tk.Turtle()
l=['purple','red','orange','blue','green','yellow']
for i in range(200):
    t.color(l[i%6])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
tk.exitonclick()