import sys
input = sys.stdin.readline

x,y,a0,a1,n=map(int, input().split())

result = [0 for i in range(100000)]
result[0]=a0
result[1]=a1

for i in range(2,n+1,1):
    result[i]=x*result[i-1]+y*result[i-2]
    result[i]=result[i]%100

print(result[n])
