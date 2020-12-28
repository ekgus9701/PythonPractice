ame=2010
capu=3020
cafe=3530
yogu=4580
total=0

print("========이화다방==========")
print("=========메뉴판=========")
print("아메리카노: 2010원")
print("카푸치노: 3020원")
print("카페라떼: 3530원")
print("요거트스무디:4580원")
print("==========================")
print()

ames=int(input("아메리카노 몇잔?"))
capus=int(input("카푸치노 몇잔?"))
cafes=int(input("카페라떼 몇잔?"))
yogus=int(input("요거트스무디 몇잔?"))
print()

total=ame*ames
total+=capu*capus
total+=cafe*cafes
total+=yogu*yogus

print("총 가격은",total,"원 입니다.")
money=int(input("얼마 내시겠습니까?"))
print()
change=money-total
coin_500s=change//500
change%=500
coin_100s=change//100
change%=100

print("기부할 돈을 뺀 거스름돈은",coin_500s*500+coin_100s*100,"원입니다.")
print("500원짜리",coin_500s,"개","100원짜리",coin_100s,"개 드릴게요")
print("기부할 돈은",change,"원입니다. 감사합니다.")
