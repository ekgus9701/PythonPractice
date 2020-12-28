def go():
    arr=[['0']*100 for k in range(100)]
   
    m=int(input(""))
    if(m%2==0 or m<1 or m>100):
        print('INPUT ERROR')
    else:
        num=0
        
        for i in range(int(m+1/2),0,-1):
            for j in range(i,m-i+2,1):
                arr[i][j]=num
                num+=1
        for i  in range(1,m+1,1):
            for j in range(1,m+1,1):
                if(arr[j][i]!='0'):
                    print("%c "%(arr[j][i]%26+65),end="")
                
            print()

go()
