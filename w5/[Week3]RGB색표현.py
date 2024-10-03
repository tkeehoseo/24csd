import turtle
win = turtle.Screen()   # Screen 객체 생성
t = turtle.Turtle()     # Turtle 객체 생성
t.pencolor(1.0, 0.0, 0.0) # 빨간색
t.fd(100)
t.pencolor(0.0, 1.0, 0.0) # 초록색
t.fd(100)
t.pencolor(0.0, 0.0, 1.0) # 파란색
t.fd(100)
t.pencolor(0.0, 1.0, 1.0) # 청록색(cyan)
t.fd(100)
t.pencolor(1.0, 0.0, 1.0) # 마젠타(magenta)
t.fd(100)

t.home()    # 초기위치로
t.clear()   # t객체가 그린 선 모두 삭제

win.colormode(255)      # 0~255 사이의 수로 RGB 색상 표현
                        # colormode는 Screen 객체의 명령!
t.pencolor(255, 0, 0)   # 빨간색
t.fd(100)
t.pencolor(0, 255, 0)   # 초록색
t.fd(100)
t.pencolor(0, 0, 255)   # 파란색
t.fd(100)
t.pencolor(0, 255, 255) # 청록색(cyan)
t.fd(100)
t.pencolor(255, 0, 255) # 마젠타(magenta)
t.fd(100)


