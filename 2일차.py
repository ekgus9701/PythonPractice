import turtle
t=turtle.Turtle()


t.color("yellow")

t.begin_fill()
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.end_fill()

t.color("green")
t.penup()
t.begin_fill()
t.pendown()
t.rt(90)
t.lt(60)
t.fd(100)
t.rt(120)
t.fd(100)
t.end_fill()


t.color("black")
t.penup()
t.rt(180)
t.fd(100)
t.rt(30)
t.pendown()
t.fd(60)
t.color("pink")
t.begin_fill()
t.rt(90)
t.circle(100)
t.end_fill()

t.color("violet")
t.begin_fill()
t.circle(80)
t.end_fill()

t.color("orange")
t.begin_fill()
t.circle(60)
t.end_fill()

t.color("red")
t.begin_fill()
t.circle(40)
t.end_fill()

t.color("white")
t.begin_fill()
t.circle(20)
t.end_fill()

