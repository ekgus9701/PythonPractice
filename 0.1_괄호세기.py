#괄호개수세기
def count():
   
    s=input("")

    여는=0
    닫는=0

    for i in range(len(s)):
        if(s[i]=='('):
            여는+=1
        if(s[i]==')'):
            닫는+=1
    print("%d %d"%(여는,닫는))

count()
        
