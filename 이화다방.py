#1971055 한다현
import random
def show_menu1():
    print()
    print("*************************ice only*************************")
    print("1.그린티 2.우롱티 3.그린밀크티 4.우롱밀크티 5.청포도스무디 0.종료")
    print("**********************************************************")

def show_menu2():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("1.밀크폼 2.펄 0.필요없음")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def get_sweet():
    sweet=int(input("당도를 고르세요(0,50,100)"))
    if(sweet==0):
        value=0
    if(sweet==50):
        value=50
    if(sweet==100):
        value=100
    return value

def get_coupon(price):
    coupon=input("이화여대생이신가요??(Y,N)")
    if(coupon=='Y' or coupon=='y'):
        print("10% 할인 해드릴게요!")
        price*=0.9
        
    if(coupon=='N' or coupon=='n'):
        print("쿠폰적용이 어렵습니다.")
        price*=1

    return price

def get_free(price):
    free=random.randint(1,100)
    if(free<=5):
        print("축하합니다! 무료이벤트 당첨!")
        price=0
    else:
        print("아쉽네요. 무료이벤트는 다음 기회에!")
        price*=1
    return price

def 밀크폼(ratio=100):
    value=500*ratio/100
    print("밀크폼  %d%%  :%d원"%(ratio,value))
    return value

def 펄():
    value=800
    print("펄 :%d원"%value)
    return value


def 얼음():
    value=200
    print("차가운 얼음  :%d원"%value)
    return value

def 그린티():
    
    print("~~~쌉싸름한 그린티를 만듭니다~~~")
    value=2500
    value+=얼음()
    return value
    
def 우롱티():
    
    print("!!!향기 좋은 우롱티를 만듭니다!!!")
    value=2800
    value+=얼음()
    return value    
    
def 그린밀크티():
    
    print("@@@쌉싸름한듯 달콤한 그린밀크티를 만듭니다@@@")
    value=그린티()
    value+=밀크폼(50)
    return value        

def 우롱밀크티():
    
    print("&&&향이 좋고 부드러운 우롱밀크티를 만듭니다&&&")
    value=우롱티()
    value+=밀크폼(50)
    return value

def 청포도스무디():
    print("^^^새콤달콤한 청포도스무디를 만듭니다^^^")
    value=3500
    value+=얼음()
    return value

def 계산(p):
    print()
    price=int(p)
    print("총 음료가격은 %d원 입니다"%price)
    pay=int(input("금액을 입력하세요"))
    
    money=pay-price
    while (money<0):
        print("금액이 음료값보다 작습니다")
        pay=int(input("금액을 다시 입력하세요"))
        money=pay-price
        if(money>=0):
                break
    print("==========================")
    print("총계산된 금액:",price)
    print("받은 금액:",pay)
    print("==========================")
    print("==> 총 %d원을 거슬러주어야합니다!"%money)
    
    m_10000s=money//10000
    money=money%10000
    m_5000s=money//5000
    money=money%5000
    m_1000s=money//1000
    money=money%1000
    m_500s=money//500
    money=money%500
    m_100s=money//100
    money=money%100

    print("10000원 개수: ",m_10000s)
    print("5000원 개수: ",m_5000s)
    print("1000원 개수: ",m_1000s)
    print("500원 개수: ",m_500s)
    print("100원 개수: ",m_100s)
    print("100원 미만인 나머지 잔돈: %d원은 불우이웃에게 기부됩니다."%money)
    

    change=m_10000s*10000+m_5000s*5000+m_1000s*1000+m_500s*500+m_100s*100

    print("받으시는 거스름돈은 %d원입니다."%change)


print("=====================================================")
print("             안녕하세요 이화다방입니다*^^*")
print("=====================================================")

price=0
total=0

while (True):
    show_menu1();
    menu1=input("메뉴:")
    
    if(menu1=='0'):
        break
    
    if(menu1!='0'):
        show_menu2();
        menu2=input("추가메뉴:")
        if(menu1=='1'):
            price=그린티()
            if (menu2=='1'):
                price+=밀크폼()
            if (menu2=='2'):
                price+=펄()
            if (menu2=='0'):
                price+=0

        if(menu1=='2'):
            price=우롱티()
            if (menu2=='1'):
                price+=밀크폼()
            if (menu2=='2'):
                price+=펄()
            if (menu2=='0'):
                price+=0

        if(menu1=='3'):
            price=그린밀크티()
            if (menu2=='1'):
                price+=밀크폼()
            if (menu2=='2'):
                price+=펄()
            if (menu2=='0'):
                price+=0

        if(menu1=='4'):
            price=우롱밀크티()
            if (menu2=='1'):
                price+=밀크폼()
            if (menu2=='2'):
                price+=펄()
            if (menu2=='0'):
                price+=0

        if(menu1=='5'):
            price=청포도스무디()
            if (menu2=='1'):
                price+=밀크폼()
            if (menu2=='2'):
                price+=펄()
            if (menu2=='0'):
                price+=0

        if(menu1<'0' or menu1>='6'):
            print("그런 메뉴는 없습니다.")
            continue
    
        price+=get_sweet()    
    print()
    print("가격:%d" %price)
    total+=price
    print("토탈가격:%d"%total)


total_p=0
total_p=get_coupon(total)
total_p=get_free(total)

print("주문을 종료합니다! %d원만큼 돈을 지불해주세요."%total_p)

계산(total_p)
