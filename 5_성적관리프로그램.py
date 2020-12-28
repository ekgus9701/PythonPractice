#성적관리프로그램
def go():
    
    list1=list(map(int,input("").split()))
    tot=0
    for i in range(len(list1)):
        
        if(list1[i]>100 or list1[i]<0):
            while(list1[i]>100 or list1[i]<0):
                list1[i]=int(input(""))
        tot+=list1[i]
    
    avg=tot/7
    max1=max(list1)
    min1=min(list1)
    print("TOT :",tot)
    print("AVG :",int(avg))
    print("MAX :",max1)
    print("MIN :",min1)
    graph(list1,avg,max1,min1)
    
def graph(list1,avg,max1,min1):
    for i in range(10,0,-1):
        if(i==10):
            print("100   ",end="")
        else:
            print(" %d   "%(i*10),end="")
        for j in range(0,7,1):
            if(list1[j]>=(i*10)):
                print("*   ",end="")
            else:
                print("    ",end="")

        if(avg>=(i*10)):
            print("*   ",end="")
        else:
            print("    ",end="")
        if(max1>=(i*10)):
            print("*   ",end="")
        else:
            print("    ",end="")
        if(min1>=(i*10)):
            print("*   ",end="")
        else:
            print("    ",end="")
        print()
    print("      A   B   C   D   E   F   G   H   I   J")



    
go()
