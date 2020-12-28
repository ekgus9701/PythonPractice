def go():
    n=int(input(""))
    
    num=0
    arr=[[0]*100 for k in range(100)]
    for j in range(n-1,-1,-1):
        for i in range(n-1,-1,-1):
            
            arr[i][j]=num
            num+=1


    for i in range(0,n,1):
        for j in range(0,n,1):
            print("%c "%(arr[i][j]%26+65),end="")
        print()

go()
