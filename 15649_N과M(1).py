import sys
input= sys.stdin.readline

N,M=input().split()
N=int(N)
M=int(M)

arr=[0]*M
isused=[False]*(N+1)


def func(k):
    if(k==M):
        for i in range(M):
            print(arr[i],end=" ")
        print()
        return
        
    for i in range(1,N+1):
        if (isused[i]==False):
            
            isused[i]=True
            arr[k]=i
            func(k+1)
            isused[i]=False

func(0)
