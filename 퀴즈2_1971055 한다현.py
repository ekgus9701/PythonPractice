############################################################################################
# 0. 화일을 내려받아 퀴즈#2_학번_이름.py로 저장합니다.
# 1. 이 화일이 잘 저장되고 실행되는지, 변경후 저장과 실행이 되는지도 F5를 눌러 확인합니다.
# 2. 코드에서 미리 정의된 변수는 변경없이 그대로 사용하고, 필요한 경우에는 추가합니다.
# 3. 각 문제의 코드는 아래 각 문제에 해당하는  def 블럭에 작성합니다.
# 4. 들여쓰기에 주의하세요
# 5. 제출하기 전, 문제에서 주어진 입력과 출력결과가 같은지 확인합니다.
# 6. 개인 PC에서 동작하는 화면을 문제당 1장씩 캡춰한 후, 코드와 함께 제출합니다.
# 7, 코드화일과 실행화면이 없는 제출은 무효입니다. 
############################################################################################



def show_menu() :
    print("--------------------------------------------")
    print(" 1. 1번   2. 2번    3. 3번      0. 종료")
    print("--------------------------------------------")

#=====================================================
# 1번문제와 관련된 함수들 
# 성적처리 : dictionary를 사용하여 과목과 과목점수를 저장합니다.
#=====================================================
def p_1() :
    #1971055 한다현
    print("===문제1===")
    ###이 아래 코드를 작성하세요.

    #주요 변수 초기화 : 순서대로 과목개수, 과목이름, 성적표
    subject_num=0
    subject_name=[]
    scoreTable={}
    total =0
    avg=0
    max_subject=0
    min_subject=0
    
    #1. 과목이름을 빈칸으로 입력받는다. 예) 국어 수학 영어 ...
    subject_name=input("과목이름을 빈칸으로 구분하여 입력하세요.").split()
    subject_num=len(subject_name)
    


    #2. 과목점수를 입력받아서, 과목이름을 key 로 하고 점수를 value로 하는 dictionary  scoreTable을 만든다. 
    # 과목점수는 0이상 100점이하이며 이 외점수는 다시 입력받는다.

    for i in range(subject_num):
        x=int(input("%s: "%subject_name[i]))
        while(True):
            if(x<0 or x>100):
                x=int(input("%s: "%subject_name[i]))
            else:
                scoreTable[subject_name[i]]=x
                break
   

    print(scoreTable) # 과목이름과 점수가 저장이 잘 되어 있는지 출력 확인

    
    #3. 과목이름, 점수, 히스토그램을 '보기'와 같이  출력한다.

    for key in scoreTable:
        sub_10s=scoreTable[key]//10
        sub_1s=scoreTable[key]%10
        print(key,": ",end="")
        for j in range(sub_10s):
            print("★",end="")
        for k in range(sub_1s):
            print("*",end="")
        print()
        



    #4. 총점, 평균, 최고점수, 최저점수를 출력하고 종료한다.

    for key in scoreTable:
        total+=scoreTable[key]
    avg=total/len(scoreTable)
    max_subject=max(scoreTable.values())
    min_subject=min(scoreTable.values())

    print("Total: %5d"%total)
    print("  Avg: %5.2lf"%avg)
    print("  max: %5d"%max_subject)
    print("  min: %5d"%min_subject)



    
#--------------------------------------------------------------------------------
#필요한 함수는 이 아래에 정의합니다.





#=====================================================
# 2번문제와 관련된 함수들
# Top
#=====================================================
def p_2() :
    print("===문제2===")
    #1971055 한다현
    
   
    

    n=int(input("탑의 개수:"))
    top=[]
    
    top=list(map(int,input("높이:").split()))

    for j in range(n):
        for i in range(j-1,-1,-1):
            if(top[j]<top[i]):
                index=i+1
                print(index,end=" ")
                break
            
            if(top[j]>top[i] and i==0):
                index=0
                print(index,end=" ")
                break
        if(j==0):
            index=0
            print(index,end=" ")
    print()






  



#--------------------------------------------------------------------------------
    
        

    
    ###이 아래 코드를 작성하세요.

#=====================================================
# 3번문제와 관련된 함수들
# 문자삼각형
#=====================================================
def p_3() :
    #1971055 한다현
    print("===문제3===")
    ###이 아래 코드를 작성하세요.
    arr=[[0]*100 for i in range(100)]
    x=0
    y=0
    
    s='A'
    n=int(input("삼각형의 크기: "))
    for i in range(0,n,1):
        x=i-1
        y=n
        for j in range(0,n-i,1):
            if(s>'Z'):
                s='A'
            x+=1
            y-=1
            
            arr[x][y]=s
            s=ord(s)
            s+=1
            s=chr(s)
    for i in range(0,n,1):
        for j in range(0,n,1):
            if(arr[i][j]==0):
                print("  ",end="")
            else:
                print("%c "%arr[i][j],end="")
        print()
                
            
            
       
        
        









#--------------------------------------------------------------------------------




################################################
# main
################################################

menu =0
while True:
    show_menu()
    menu=input("menu:")
    
    # 메뉴에 따라 올바르게 동작하는 비교문을 작성하세요
    if (menu=='0') :
        print("수고하셨습니다")
        break
    if(menu=='1'): p_1()
    if(menu=='2'):p_2()
    if(menu=='3'):p_3()
    if(menu>'3' or menu<'1'):
        print("그런 메뉴는 없습니다.")
            
    




	



################################################

