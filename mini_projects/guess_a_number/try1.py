import random

def guess_a_num():
    # Difficulty level
    level = int(input("Press 1 for 'Easy', press 2 for 'Hard': "))

    # Randomly choose a number below 100
    number = random.randint(0, 100)
    print(f"Secret number: {number}")  # For testing purposes

    def no_of_turns(lvl):
        if lvl == 1:
            return 10
        elif lvl == 2:
            return 5
        else:
            return 0  # Invalid level

    def compare(guessed):
        if guessed == number:
            print("Your guess is right!")
            return True  # Exit the game if guessed correctly
        elif guessed > number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
        return False

    for i in range(no_of_turns(level)):
        guess = int(input("Enter a number: "))
        if compare(guess):
            break

guess_a_num()

