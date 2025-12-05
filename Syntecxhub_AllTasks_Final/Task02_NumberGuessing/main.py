import random

def main():
    print("=== Number Guessing Game ===")
    target = random.randint(1, 100)

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Please enter numbers only!")
            continue

        if guess == target:
            print("🎉 Correct! You guessed it!")
            break
        elif guess < target:
            print("Too low!")
        else:
            print("Too high!")

if __name__ == "__main__":
    main()
