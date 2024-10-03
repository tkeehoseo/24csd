import turtle
win = turtle.Screen()
win.bgcolor('azure')             # 윈도우 색 변경
t = turtle.Turtle()
len = 50
t.pensize(30)
t.penup()
t.goto(-win.window_width()/2,0) # 시작위치로 이동
t.pendown()
t.pencolor('dark salmon'); t.forward(len)
t.pencolor('salmon'); t.forward(len)
t.pencolor('light salmon'); t.forward(len)
t.pencolor('orange'); t.forward(len)
t.pencolor('dark orange'); t.forward(len)
t.pencolor('coral'); t.forward(len)
t.pencolor('light coral'); t.forward(len)
t.pencolor('tomato'); t.forward(len)
t.pencolor('orange red'); t.forward(len)
t.pencolor('red'); t.forward(len)

