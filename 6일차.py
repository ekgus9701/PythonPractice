#야구게임

s=0
o=0
b=0

com="1324"
me=input("수를 입력하세요")

for i in range(4):
    print(me[i],":",com[i])
    j=com.find(me[i])
    print("i: ",i,", j: ",j)
    if(j==i):
        s+=1
    elif(j!=i and j>0):
        b+=1
o=4-s-b

print("strike",s)
print("ball",b)
print("out",o)

    
    
    
