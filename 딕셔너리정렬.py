phone_book={}
phone_book["길동"]="1234"
phone_book["감찬"]="5678"
phone_book["순신"]="9012"

for i in sorted(phone_book.values()):
    print(i,phone_book[i])
