'''
    변수를 사용한 정삼각형 그리기 코드
    여러 줄을 주석으로 표시할 때는
    작은 따옴표 혹은 큰 따옴표 3개로
    그 시작과 끝을 표시
'''
# 한 줄 주석은 특수기호 #으로 삽입
# 코드에서 사용할 변수 저장
width = 500             # 윈도우 가로 길이를 width라는 변수에 저장
height = 500            # 윈도우 세로 길이를 height라는 변수에 저장
lineLength = 100        # 정삼각형 한 변의 길이를 lineLength라는 변수에 저장
diffAngle = 120         # 정삼각형 꼭지점에서 회전해야 할 각도를 diffAngle 변수에 저장

import turtle   # 거북이 그래픽 모듈 가져오기
win = turtle.Screen()   # 윈도우 객체를 생성하여 win 변수에 저장(대입)

win.setup(width,height)      # setup 명령은 윈도우 관련 명령이므로 윈도우 객체인 win을 통해 명령 전달
t = turtle.Turtle()     # 거북이 객체를 생성하여 t 변수에 대입
t.fd(lineLength)               # t라는 거북이 객체에 이동/회전 명령을 전달
t.right(diffAngle)
t.fd(lineLength)
t.right(diffAngle)
t.fd(lineLength)
