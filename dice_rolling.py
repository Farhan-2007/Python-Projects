from random import randint

total_rolls = 0
while True:

    choice = input("Enter your choice y/n ? ").lower()
    rolls = int(input("How many dice you want to roll? "))

    if choice == "y":
        total_rolls += 1
        die1 = [randint(1,6) for i in range(rolls)]
        die2 = [randint(1,6) for i in range(rolls)]
        print(f"In Die 1 rolls {die1} appeared")
        print(f"In Die 2 rolls {die2} appeared")
        print(f"This time you had roll dice {rolls} times")
        print(f"You had roll dice this many {total_rolls} times")
    
    elif choice == "n":
        print("Thanks for playing")
        break
    
    else:
        print("Invalid choice")

