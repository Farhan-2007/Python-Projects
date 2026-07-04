from random import randint
numbers = randint(1, 100)
attempts = 0 

while True:

    try:
        guess = int(input("Enter your number between 1 to 100: "))
        attempts += 1
        if guess > numbers:
            print("Please Enter Lower Number!")
        elif guess < numbers:
            print("Please Enter Higher Number!")
        elif guess == numbers:
            print(f"Congratulation you guess the correct number {guess} in {attempts} attempts")
            break
    except ValueError:
        print("invalid Choice")