#1971055 한다현

def get_menu():
    print("======================menu======================")
    print("1.영화표 예약하기 2.영화표 취소하기 3.간식 사기 0.종료")
    menu=input("메뉴를 고르세요")
    return menu

def get_movie():
    print("=================================영화시간표===================================")
    print("1.해리포터와 불의잔(11:00) 2.헝거게임(13:00) 3.미비포유(17:00) 4.부산행(21:00)")
    print("==============================================================================")
    movie=input("어떤 영화를 보시겠습니까?")
    if(movie=='1'):
        value=11000
    if(movie=='2'):
        value=11000
    if(movie=='3'):
        value=11000
    if(movie=='4'):
        value=11000
    return value

def get_people(value):
    people=int(input("사람수는 몇명입니까?"))
    value*=people
    return value,people

def show_seat(seat,row,col):
    for r in range(0,row):
        print("%2d: "%(r+1),end=" ")
        for c in range(0,col):
            if(seat[r][c]==0): print("□",end=" ")
            else: print("■",end=" ")
        print()

def get_seat(seat,r,c):
    if (seat[r][c]==0):
         seat[r][c]=1
    else:
        print("이미 예약된 좌석입니다! 다시입력하세요")
        r1=int(input("앉으실 행을 입력: "))
        c1=int(input("앉으실 열을 입력: "))
        get_seat(data,r1-1,c1-1)
        print()
    show_seat(data,row,col)
        
        
def cancel_seat(seat,r,c,price):
    if (seat[r][c]==0):
            print("예약된 적이 없는 좌석입니다!")
    else:
        seat[r][c]=0
        print("예약이 취소되었습니다.")
        price-=11000
        
    show_seat(data,row,col)
    return price
            
            
def buy_food():
    price=0
    while(True):
        print("================간식================")
        print("1.팝콘 2.콜라 3.버터오징어 0.종료")
        print("====================================")
        menu=input("메뉴")
        
        if(menu=='0'):
            print("간식 주문을 종료합니다.")
            break
        if(menu=='1'):
            price+=6000
            print("@@@@고소한 팝콘을 준비해드릴게요@@@@")
        if(menu=='2'):
            price+=2500
            print("@@@@시원한 콜라를 준비해드릴게요@@@@")
        if(menu=='3'):
            price+=4000
            print("@@@@쫄깃한 버터오징어를 준비해드릴게요@@@@")
        if(menu>'3' or menu<'0'):
            print("다시 주문해주세요")
        
    return price
            

def 계산(p):
    print()
    price=int(p)
    print("총 가격은 %d원 입니다"%price)
    pay=int(input("금액을 입력하세요"))
    
    money=pay-price
    while (money<0):
        print("금액이 값보다 작습니다")
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

#main
total=0

while(True):
    
    menu=get_menu()
    if(menu=='0'):
        print("종료합니다.")
        
        break
    if(menu=='1'):
    
        money=get_movie()
        money1,people=get_people(money)
        total+=money1
        print()
        print("2차원 배열을 만들어 0으로 초기화합니다.")
        row=int(input("행: "))
        col=int(input("열: "))
        data=[[0]*col for j in range(row)]

        show_seat(data,row,col)
        for i in range(people):
            print("%d번째 사람의 자리를 예약합니다."%(i+1))
            r1=int(input("앉으실 행을 입력: "))
            c1=int(input("앉으실 열을 입력: "))
            get_seat(data,r1-1,c1-1)
           

    if(menu=='2'):
        r1=int(input("취소하실 행을 입력: "))
        c1=int(input("취소하실 열을 입력: "))
        total=cancel_seat(data,r1-1,c1-1,total)
       
 
    if(menu=='3'):
        money2=buy_food()
        total+=money2
        

계산(total)
        
        
    


    
    
