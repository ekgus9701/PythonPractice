x=int(input("뭔 배수?"))
y=int(input("1?"))
z=int(input("2?"))
while True:
 for i in range(y,z+1,x) :
      if  (i%x)!=0 :
        print((i+x)//x*x)
      else:
        print (i)
        
