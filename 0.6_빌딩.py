#빌딩
def go():
    n=int(input(""))
    building=[]
    for i in range(n):
        building.append(int(input("")))

    for j in range(n):
        for i in range(j+1,n,1):
            if(building[j]<building[i]):
                index=i+1
                print(index)
                break
            #오른쪽에 큰게 없을때
            if(building[j]>building[i] and i==n-1):
                index=0
                print(index)
        if(j==n-1):#가장 오른쪽 빌딩일때
            index=0
            print(index)
    

go()
