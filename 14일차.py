#1971055 한다현

import random
def show_words(fail):
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
            fail+=1
            print()
    return fail

guesses=''
turns=10
infile=open("C:\\Users\\lg\\Desktop\\words.txt")
lines=infile.readlines()
word=random.choice(lines)
word=word.strip()

while True:
    if turns==0:
        print("사용자 패배 정답은"+word)
        break
    failed=0
    failed=show_words(failed)
    if failed==0:
        print("사용자 승리!")
        break

    guess=input("단어를 추측하시오[%d] :"%turns)
    guesses+=guess
    if guess not in word:
        turns-=1
        print("틀렸습니다 "+str(turns)+"번의 기회가 남았습니다!")
infile.close()
