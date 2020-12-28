#1971055 한다현
#------------------------------------
import random
import os

def makeTeam(team,name,n):
    memberNo=[]
    i=0
    while True:
        
        if(len(memberNo)==n):
            break
        num=random.randint(0,len(player)-1)

        if(num not in memberNo):
            memberNo.append(num)
        else:
            continue
        i+=1
    for i in range(n):
        team.append(player[memberNo[i]].copy())
        team[i][0]+=name
    return team
        
def showTeam(team,name):
    print("--------------------------------------------------------")
    print(" %s - %d 명"%(name,len(team)))
    print("--------------------------------------------------------")
    print("   이름                      hp     power   skill")
    print("--------------------------------------------------------")
    for i in range(len(team)):
        print("%s  : %10d   %5d   %s"%(team[i][0],team[i][1],team[i][2],team[i][3]))

def showTeams(team1,name1,team2,name2,num):
    print("------------------------------------------------------------------------------------------------------")
    print(" %s - %d 명                                           %s - %d 명"%(name1,len(team1),name2,len(team2)))
    print("------------------------------------------------------------------------------------------------------")
    print("이름                 hp   power    skill          이름                 hp   power    skill          ")
    print("------------------------------------------------------------------------------------------------------")
    for i in range(num):
        
        if(i<len(team1)):
            print("%s %5d %5d %s    "%(team1[i][0],team1[i][1],team1[i][2],team1[i][3]),end="")
        else:
            print("                                                 ",end="")
        if(i<len(team2)):
            print("%s %5d %5d %s "%(team2[i][0],team2[i][1],team2[i][2],team2[i][3]))
        else:
            print()
    print("------------------------------------------------------------------------------------------------------")

def attack(team1,team2):
    attacker=team1[random.randint(0,len(team1)-1)]
    target=team2[random.randint(0,len(team2)-1)]
    print("%s가 %s를 %s스킬로 공격합니다!"%(attacker[0],target[0],attacker[3]))

    target[1]-=attacker[2]
    if(target[1]<0):
        print(target[0],"가 죽었습니다")
        team2.remove(target) 
        
    

#=============================================================main======================================================================

player=[['해리포터★',1000,500,"엑스펠리아무스"],['헤르미온느',800,550,"듀로＠＠＠＠＠"],['●◈론♡♣',1100,450,"디미누엔도＠＠"],
        ['◑말포이⊙',900,500,"글레시우스＠＠"],['볼드모트○',1300,600,"크루시오＠＠＠"],['덤블도어◀',1200,650,"임페리오＠＠＠"]]
win=0

print("누가 이길것같나요?")
ask=int(input("호그와트는 1, 호구와트는 2를 눌러주세요"))
print()

호구와트=[]
호그와트=[]
name1="(마술사)"
name2="(마법사)"
호구와트=makeTeam(호구와트,name1,3)
showTeam(호구와트,name1)
호그와트=makeTeam(호그와트,name2,3)

showTeam(호그와트,name2)
print("***********************Battle Start!**************************")
showTeams(호구와트,name1,호그와트,name2,3)
while(True):
    rd=random.randint(0,1)
    if(rd==1):
        attack(호구와트,호그와트)
        showTeams(호구와트,name1,호그와트,name2,3)
    if(rd==0):
        attack(호그와트,호구와트)
        showTeams(호구와트,name1,호그와트,name2,3)
    if(not 호구와트):
        win=1
        break
    if(not 호그와트):
        win=2
        break
if(win==1):
    print("호그와트가 이겼습니다!")
    if(ask==1):
        print("이긴 팀을 맞추셨네요! 축하합니다~")
    if(ask==2):
        print("아쉽게 틀리셨네요")
if(win==2):
    print("호구와트가 이겼습니다!")
    if(ask==2):
        print("이긴 팀을 맞추셨네요! 축하합니다~")
    if(ask==1):
        print("아쉽게 틀리셨네요")

os.system("pause")
          
    



