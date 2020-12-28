# 토끼와 거북이의 경주
# (space 키) : 토끼와 거북이는 출발선에 서서 달려 나간다.
# (r 키) : 경주 후에 결과를 출력한다.

import turtle
import random

image1 = "C:/Users/lg/Desktop/초록쿠키.gif"
image2 = "C:/Users/lg/Desktop/파란쿠키.gif"
turtle.addshape(image1)
turtle.addshape(image2)

r = turtle.Turtle(image1)
t = turtle.Turtle(image2)

t.up(); t.goto(-200, 0)  # 출발선으로 이동
r.up(); r.goto(-200, 200)  # 출발선으로 이동

def run():
    for i in range (200) :
        r.forward(random.randint(1, 5))        
        t.forward(random.randint(1, 5))
    global rpos, tpos
    rpos = r.position()  # 경주 끝날 때의 토끼 위치
    tpos = t.position()  # 경주 끝날 때의 거북이 위치

rpos = -200; tpos = -200  # 출발점의 x 좌표 저장

def result():   # 경주 결과 출력
    if rpos[0] > tpos[0] :
        print("토끼가 이겼다")
    elif rpos[0] == tpos[0] :
        print("비겼다")
    else :
        print("거북이가 이겼다")            

turtle.onkey(run, "space")  # 경주 시작을 알린다
turtle.onkey(result, "r")   # 경주 결과를 출력한다
turtle.listen()  
