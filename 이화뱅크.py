#=============================
#1971055 한다현
#=============================

def deposit(start,end,total,goal):
    print(start,",",end)
    for i in range(start,end+1):
        if(goal<=total):
            print("축하축하! 목표금액 달성!!!")
            print("예금을 종료합니다!")
            break;
        total+=money+total*rate/1200
        print("  %3d    %10d    %5.2f     %20.2f"%(i,money,rate/12,total))
    return total

def spend(total):
    count=1
    print("현재 가지고 계신 돈은 %d원입니다."%(total))
    money1=int(input("한달 이체할 돈을 정해주세요"))
    name=input("누구의 통장으로 이체하시겠습니까?")
    num=int(input("계좌번호가 무엇인가요?"))
    
    print("한달에 자동으로 %s님의 통장(계좌번호: %d)으로 %d원만큼 이체됩니다."%(name,num,money1))
    print("회차    총")
    while(True):
        total-=money1
        if(total<=0):
            print("%d달차 자동이체가 불가합니다. 돈이 부족합니다! "%count)
            print("모으신 돈으로 총 %d달동안 자동이체를 하셨네요!"%(count-1))
            break;
        else:
            print("%d    %d"%(count,total))
            count+=1
        
            
print("------------------------------------------------")
print("----------이화뱅크에 오신걸 환영합니다----------")
print("------------------------------------------------")
rate=float(input("저축이율을 입력하세요(연%): "))
money=int(input("한달에 저축할 금액: "))
term=int(input("얼마동안 저축할까요?(월): "))
goal=int(input("목표액은 얼마인가요?(월): "))    
total=0;
print("------------------------------------------------")
print("   회차    입금액     이율(월%)                총")
total=deposit(1,term,total,goal)

left=goal-total
if(left<0):
        print("축하합니다! 목표금액을 달성하셨습니다!!")
else:
        print("목표금액까지 %.2f원이 부족합니다."%left)
        print("지금부터 약 %d개월 더 저축하면 됩니다."%(left//money))
        answer=input("저축을 이어서 계속하시겠습니까?(Y,N) : ")
        if(answer=='Y' or answer=='y'):
            total = deposit(term+1,term+1+int(left//money),total,goal)

spend(total)

print("이화뱅크를 사용해주셔서 감사합니다!")
