#빌딩
def go():
    n=int(input(""))
    top=[]
    
    top=list(map(int,input().split()))

    for j in range(n):
        for i in range(j-1,-1,-1):
            if(top[j]<top[i]):
                index=i+1
                print(index,end=" ")
                break
            
            if(top[j]>top[i] and i==0):
                index=0
                print(index,end=" ")
                break
        if(j==0):
            index=0
            print(index,end=" ")
    

go()
