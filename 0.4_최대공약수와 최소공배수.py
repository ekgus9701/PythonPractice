#최대공약수와 최소공배수
def go():
    a, b=input("").split()
    a=int(a)
    b=int(b)
    
    gcd=get_gcd(a,b)
    lcm=a*b/gcd
    lcm=int(lcm)
    print(gcd)
    print(lcm)


def get_gcd(a,b):
   while True:
       if(b==0):
           break
       r=a%b
       a=b
       b=r
   return a


go()
