import random

print("🎮 NUMBER GUESSING GAME 🎮")
print("I'm thinking of a number between 1 and 100!")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("📈 Too low! Try again.")
    elif guess > number:
        print("📉 Too high! Try again.")
    else:
        print("🎉 YOU WON! 🎉")
        print("The number was:", number)
        print("You needed", attempts, "tries!")
        break