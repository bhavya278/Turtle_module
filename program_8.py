import turtle as tk
t=tk.Turtle()
l=['yellow','red','blue','green']
t.up()
t.goto(200,0)
for i in range(4):
    t.down()
    t.begin_fill()
    t.fillcolor(l[i])
    t.circle(50)
    t.end_fill()
    t.up()
    t.bk(100)
tk.exitonclick()