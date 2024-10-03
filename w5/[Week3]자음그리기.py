import turtle
win = turtle.Screen()           # window 객체 생성
w = 1000
h = 500
offset = 100                    # 위 여백
win.setup(w,h)                  # window 크기 설정
t = turtle.Turtle('circle')     # 거북이 객체 생성(기본 모양 중 '원'모양)
size = int(input('글자 크기: '))# 글자 크기(한 변의 길이) 입력 받기
t.speed(10)                     # 그리기 속도 설정

# 'ㄱ' 그리기
t.penup()                   # 펜 올리기
t.goto(-w/2,h/2-offset)     # 시작 위치로 이동
t.pendown()                 # 펜 내리기
t.forward(size)
t.right(90)
t.forward(size)

# 'ㄴ' 그리기
t.penup()                   # 펜 올리기
t.goto(-w/4,h/2-offset)     # 시작 위치로 이동
t.setheading(0)             # 방향 초기화
t.pendown()                 # 펜 내리기
t.right(90)
t.forward(size)
t.left(90)
t.forward(size)

# 'ㄷ' 그리기
t.penup()                   # 펜 올리기
t.goto(0,h/2-offset)        # 시작 위치로 이동
t.setheading(0)             # 방향 초기화
t.pendown()                 # 펜 내리기
t.backward(size)
t.right(90)
t.forward(size)
t.left(90)
t.forward(size)
'''
# 글씨쓰는 방식
t.forward(size)
t.penup()
t.goto(0,h/2-offset)        # 시작 위치로 이동
t.pendown()
t.right(90)
t.forward(size)
t.left(90)
t.forward(size)
'''
# 'ㄹ' 그리기
t.penup()                   # 펜 올리기
t.goto(w/4,h/2-offset)      # 시작 위치로 이동
t.setheading(0)             # 방향 초기화
t.pendown()                 # 펜 내리기
t.forward(size)
t.right(90)
t.forward(size/2)
t.right(90)
t.forward(size)
t.left(90)
t.forward(size/2)
t.left(90)
t.forward(size)


       
