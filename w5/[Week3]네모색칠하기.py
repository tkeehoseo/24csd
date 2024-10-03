import turtle           # turtle 모듈 불러오기
win = turtle.Screen()   # Screen 객체 생성
t = turtle.Turtle()     # Turtle 객체 생성
t.fillcolor('sky blue') # 색칠할 색상 설정
t.begin_fill()          # 색칠 시작
t.forward(100)          # 영역 그리기
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()            # 색칠 종료
