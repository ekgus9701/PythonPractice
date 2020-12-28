import sys
input = sys.stdin.readline

s=input()
check0=False
check1=False
check2=False
check3=False
for i in range(len(s)):
    if(s[i]=='U'):
        check0=True
    if(s[i]=='C'):
        if(check0):
            check1=True    
    if(s[i]=='P'):
        if(check1):
            check2=True
    if(s[i]=='C' and i>s.find('P')):
        if(check2):
            check3=True
            break
if(check3):
    print("I love UCPC")
else:
    print("I hate UCPC")
        
    

