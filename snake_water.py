import random


computer  = random.choice([1,0,-1])
youstart = input("Enter Your Choice : ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict =  {1 : "Snake", -1 : "Water", 0 : "Gun" }
you = youDict[youstart]

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Draw")
 
else:
    if(computer == -1 and you == 1):
        print("You Won")

    elif(computer == -1 and you == 0):
            print("Computer Wins")

    if(computer == 1 and you == -1):
        print("Computer Wins")

    elif(computer == 1 and you == 0):
        print("You Win")

    if(computer == 0 and you == 1):
        print("Computer Wins")

    elif(computer == 0 and you == -1):
        print("You Win")
    
    else:
         print("Something Went Wrong")