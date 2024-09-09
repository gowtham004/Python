import random
from art import art

def guess_a_num():
    print(art)
    # Difficulty level
    level = int(input("Press 1 for 'Easy', press 2 for 'Hard': "))

    # Randomly choose a number below 100
    number = random.randint(0, 100)
    #print(f"Secret number: {number}")  # For testing purposes

    def no_of_turns(lvl):
        if lvl == 1:
            return 10
        elif lvl == 2:
            return 5
        else:
            return 0  # Invalid level

    def compare(guessed, turns_left):
        if guessed == number:
            print("Your guess is right!")
            return True  # Exit the game if guessed correctly
        elif guessed > number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
        print(f"Turns left: {turns_left} \nGuess again")
        return False

    for i in range(no_of_turns(level)):
        guess = int(input("Enter a number: "))
        if compare(guess, no_of_turns(level) - i - 1):
            break

guess_a_num()

while input('Press \'Y\' to continue, \'N\' to quit: ').upper() == 'Y':
    print('\n' * 20)
    guess_a_num()
