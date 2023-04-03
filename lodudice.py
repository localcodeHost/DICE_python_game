import random
# game limit
print("welcome to dice game ")
print()
game_round=int(input("enter round limits : ="))
# gam score
score=0
# total point
total = 0
for i in range(game_round):
    # user dice trow permission
    user= input(" trow dice (t) /n :=  ")
# trow dice random numbers
    num1= random.randint(1,6)
    num2= random.randint(1,6)
   
    # permission logic
    if user.lower()=="t":
        print("dice number is ", num1 , ":", num2)
        # game win logic
        if num1==num2:
            score=score+1
            print("your point: ",score)
       
     
    elif user.lower()=="n":
        break
    else:
        print("invalid key ")
        break
print("GAME OVER") 
total = score
print("your total point is ", total)

if score<=0:
    print("you lose game")
elif score>2:
    print("welcome you win the game")

input()


