#불쾌한 날
def go():
    n=int(input(""))
    cow=[]
    sum=0
    for i in range(n):
        cow.append(int(input("")))

    for j in range(n):
        for k in range(j+1,n,1):
            if(cow[j]>cow[k]):
                
                sum+=1
            if(cow[j]<=cow[k]):
                break
                
            
        
    print(sum)
    

go()
