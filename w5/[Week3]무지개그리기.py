rainbow_size = 500      # 무지개 크기(너비)
pen_size = 30           # 펜 굵기
import turtle
win = turtle.Screen()   # Screen 객체 생성
t = turtle.Turtle()     # Turtle 객체 생성
t.pensize(pen_size)     # 펜 굵기 설정
t.speed(10)             # 그리기 속도 설정

t.setheading(90)        # 위 쪽을 바라보도록 방향 설정
t.penup()
t.setpos(rainbow_size/2,0)      # 빨간색 반원 시작 위치로 이동
t.pendown()
t.pencolor('red')
t.circle(rainbow_size/2,180)    # 무지개 크기의 반을 반지름으로
                                # 180도 반시계방향으로 회전한 반원 그리기
t.setheading(90)        # 위 쪽을 바라보도록 방향 설정
t.penup()
t.setpos(rainbow_size/2-pen_size,0) # 주황색 반원 시작 위치로 이동
t.pendown()
t.pencolor('orange')
t.circle(rainbow_size/2-pen_size,180)    # 반지름을 줄인 주황색 반원 그리기

t.setheading(90)        # 위 쪽을 바라보도록 방향 설정
t.penup()
t.setpos(rainbow_size/2-2*pen_size,0) # 노랑색 반원 시작 위치로 이동
t.pendown()
t.pencolor('yellow')
t.circle(rainbow_size/2-2*pen_size,180)    # 반지름을 줄인 노랑색 반원 그리기

t.setheading(90)        # 위 쪽을 바라보도록 방향 설정
t.penup()
t.setpos(rainbow_size/2-3*pen_size,0) # 초록색 반원 시작 위치로 이동
t.pendown()
t.pencolor('green')
t.circle(rainbow_size/2-3*pen_size,180)    # 반지름을 줄인 초록색 반원 그리기

t.setheading(90)        # 위 쪽을 바라보도록 방향 설정
t.penup()
t.setpos(rainbow_size/2-4*pen_size,0) # 파랑색 반원 시작 위치로 이동
t.pendown()
t.pencolor('blue')
t.circle(rainbow_size/2-4*pen_size,180)    # 반지름을 줄인 파랑색 반원 그리기

t.setheading(90)        # 위 쪽을 바라보도록 방향 설정
t.penup()
t.setpos(rainbow_size/2-5*pen_size,0) # 남색 반원 시작 위치로 이동
t.pendown()
t.pencolor('navy')
t.circle(rainbow_size/2-5*pen_size,180)    # 반지름을 줄인 남색 반원 그리기

t.setheading(90)        # 위 쪽을 바라보도록 방향 설정
t.penup()
t.setpos(rainbow_size/2-6*pen_size,0) # 보라색 반원 시작 위치로 이동
t.pendown()
t.pencolor('purple')
t.circle(rainbow_size/2-6*pen_size,180)    # 반지름을 줄인 보라색 반원 그리기
