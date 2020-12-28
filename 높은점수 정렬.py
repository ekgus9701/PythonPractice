i=0
listV=[]
listV_R=[]
listV_S=[]
while(True):
    nV=int(input("입력받을 개수 입력:"))
    if(nV>20):
        print("20 이하 정수입력")
        continue
    

    for grade in range(nV):
        print(grade+1,end="")
        grade=int(input("번째 점수입력:"))
        i+=1
        ListV.append(grade);
        
    if(i==3):
        break;
        
    
ListV_S=sorted(listV)
print("입력된 점수:",str(listV))
printf("높은 점수부터 정렬:",str(ListV_S))

