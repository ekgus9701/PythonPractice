def go():
    a,b,c=map(int,input("").split())
    max1=max(a,b,c)
    min1=(min(a,b,c))
    mid=a+b+c-max1-min1

    print("%d %d %d"%(min1,mid,max1))

go()
