#1971055 한다현
print("1971055 한다현 코드")
####################
#함수정의


def get_sum(a,b):
    sum=a+b
    print("%d+%d=%d"%(a,b,sum))
    print()
    return sum

def get_subt(a,b):
    subt=a-b
    print("%d-%d=%d"%(a,b,subt))
    print()
    return subt

def get_prod(a,b):
    prod=a*b
    print("%d*%d=%d"%(a,b,prod))
    print()
    return prod

def get_div_1(a,b):
    if(b==0):
        print("0으로 나눌 수 없습니다")
        print("= 0")
        print()
    else:
        div_1=a//b
        print("%d//%d=%d"%(a,b,div_1))
        print()
        return div_1

def get_div_2(a,b):
    if(b==0):
        print("0으로 나눌 수 없습니다")
        print("= 0")
        print()
    else:
        div_2=a%b
        print("%d%%%d=%d"%(a,b,div_2))
        print()
        return div_2

def get_input():
    num=int(input("정수: "))
   
    return num

def get_break():
    print("종료합니다")
    print()


###############################
##main 정의

print("----------------------------------------------------------------------")
print("1.더하기 2.빼기 3.곱하기 4.나누기(몫) 5.나누기(나머지) 6.두정수 입력받기 0.종료")
print("----------------------------------------------------------------------")
while(True):
    menu=int(input("menu:"))

    if(menu==0):
        get_break();
        break;

    if(menu==1):
        result=get_sum(a,b)
        

    if(menu==2):
        result=get_subt(a,b)
        

    if(menu==3):
        result=get_prod(a,b)

    if(menu==4):
        result=get_div_1(a,b)

    if(menu==5):
        result=get_div_2(a,b)

    if(menu==6):
        a=get_input()
        b=get_input()
        continue
    
    else:
        print("그런 메뉴는 없습니다.")
        continue
        
    
        
    

