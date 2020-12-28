#1971055 한다현
#######################
print("1971055 한다현")
#######################
def fact(n):
    print(n,end="*")
    if(n==1):
        return 1
    if(n>1):
        return fact(n-1)*n

    
################################
n=5
result=fact(n)
print()
print("%d!=%d"%(n,result))
