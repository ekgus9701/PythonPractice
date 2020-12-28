#함수로 원하는 값의 위치 리턴하기 1

def loc():
    n=int(input())
    data=list(map(int,input().split()))
    k=int(input())
    for i in range(n):
       if(data[i]==k):
           index=i+1
           break
       else:
           index=-1
    print(index)

loc()
    
    

