#program_7 done this same thing but with the help of functions

import turtle as tk
t=tk.Turtle()
t.up()
t.goto(0,-50)
t.down()
t.begin_fill()
t.fillcolor('green')
t.down()
t.circle(50)
t.end_fill()
t.up()
t.home()
t.goto(200,200)
t.down()
t.begin_fill()
t.fillcolor('orange')
t.down()
t.circle(50)
t.end_fill()
t.up()
t.goto(-200,200)
t.down()
t.begin_fill()
t.fillcolor('blue')
t.down()
t.circle(50)
t.end_fill()

t.up()
t.goto(-200,-200)
t.down()
t.begin_fill()
t.fillcolor('red')
t.down()
t.circle(-50)
t.end_fill()

t.up()
t.goto(200,-200)
t.down()
t.begin_fill()
t.fillcolor('yellow')
t.down()
t.circle(-50)
t.end_fill()
t.hideturtle()
tk.exitonclick()