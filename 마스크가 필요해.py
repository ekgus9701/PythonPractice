#마스크가 필요해
import sys
input = sys.stdin.readline

N,M=input().split()
N=int(N)
M=int(M)

data1 =[[int(x) for x in input().split()]for y in range(N)]
data2 =[[int(x) for x in input().split()]for y in range(M)]
print(data1)
print(data2)
sum=0
for i in range(N):
    for j in range(M):
        if(data1[i][0] < data2[j][0] and data1[i][1] < data2[j][0]):
            N-=1
   
print(sum)

