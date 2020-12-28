phone_book={}
phone_book["홍길동"]="01012345678"

phone_book["홍길"]="0112345678"
phone_book["길동"]="010123456"
print(phone_book.keys())
print(phone_book.values())
for i in sorted(phone_book.values()):
    print(i,phone_book[i])
