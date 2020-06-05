import turtle as tk
t=tk.Turtle()
l=['yellow','red','blue','green']
t.up()
t.goto(200,0)
for i in range(4):
    t.down()
    t.color(l[i])
    t.pensize(20)
    t.circle(100)
    t.up()
    t.bk(100)
tk.exitonclick()