#7일차
#주어진 rgb 빛들을 다르게 섞어 만들 수 있는 모든 경우의 조합(r g b)과
#총 가짓 수를 계산해보자.


r,g,b=input("").split()
r=int(r)
g=int(g)
b=int(b)


sum=0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            sum+=1

print(sum)
