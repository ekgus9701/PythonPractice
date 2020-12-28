import random

def makeTeam(team,name,n):
    
    memberNo=[]
    i=0
    while True :
        print(memberNo)
        if(len(memberNo)==n): break
        num=random.randint(0,len(player)-1)

        if(num not in memberNo):
            memberNo.append(num)
        else:
            print("중복")
            continue
        i+=1

    for i in range(n):
        team.append(player[memberNo[i]].copy())

        team[i][0]+=name
        

def showTeam(team,name):
    print("----------------------------------------------------------------------------------------")
    print("%s-%d명"%(name,len(team)))
    print("----------------------------------------------------------------------------------------")
    print("      이름   :             hp        power")
    print("----------------------------------------------------------------------------------------")
    for i in range(len(team)):
        print("%s :%10d %5d"%(team[i][0],team[i][1],team[i][2]))


def showTeams(team1,name1, team2,name2, num=3):
    print("----------------------------------------------------------------------------------------")
    print("%s - %d 명                  %s - %d명 "%(name1,len(team1),name2,len(team2)))
    print("----------------------------------------------------------------------------------------")
    print("    이름                  hp         power ㅣ  이름              hp         power")
    print("----------------------------------------------------------------------------------------")

    for i in range(3):
        if(i<len(team1)):
            print("%s:%6d%5d  "%(team1[i][0],team1[i][1],team1[i][2]), end="")
        else : print("                                  ",end="")

        if (i<len(team2)) : print("%s : %6d%5d"%(team2[i][0],team2[i][1],team2[i][2]))
        else : print()
    print("---------------------------------------------------------------------------------------")

def attack(team1,team2):
    attacker=team1[random.randint(0,len(team1)-1)]
    target=team2[random.randint(0,len(team2)-1)]

    target[1]=target[1]-attacker[2]
    

    if(target[1]<=0):
        team2.remove(target)
    


name=["A", "B"]
player=[['송지효',2000,300],['이광수',3000,500],['전소민',1000,200],['양세찬',2000,250],['김종국',4000,600],['유재석',2000,400]]
print("player :",end="")
print(player)
teamA=[]
teamB=[]
makeTeam(teamA,name[0],3)
showTeam(teamA,name[0])
makeTeam(teamB,name[1],3)
showTeam(teamB,name[1])
showTeams(teamA,name[0], teamB,name[1], 3)
attack(teamA,teamB)
showTeams(teamA,name[0], teamB,name[1], 3)
