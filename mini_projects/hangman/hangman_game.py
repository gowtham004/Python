import random

from hangman_art import hangmanpics
from hangman_words import word_list

print("find The Character")
# creating list of words

# selecting random name from list
chosen_word = random.choice(word_list)
#print(chosen_word)  # created for testing

# print the no of _ required
place_holder = []
for _ in range(len(chosen_word)):
    place_holder.append("_")
print(place_holder)

# no of wrong guess user can make
lives = 6
# necessary for looping and reducing lives
correct_guess = False
# to loop the guessing part
while lives > 0 and "_" in place_holder:
    # ask the user to guess a letter
    guess = input("Enter a letter : ").upper()

    # to check if the letter is already there or not
    if guess in place_holder:
        print("Already guessed!!!")
        print(f"You have {lives} lives left.")
        print(place_holder)
        print(hangmanpics[-(lives + 1)])
        continue  # Continue the loop without breaking it
    # necessary for looping and reducing lives
    correct_guess = False
    for index, letter in enumerate(chosen_word):

        # to enter if the guessed letter is right and flag true
        if guess in letter:
            place_holder[index] = letter
            correct_guess = True

    # to print if the guess is right
    if correct_guess:
        print(f"Correct guess! You have {lives} lives left.")
    else:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")

    print(place_holder)
    print(hangmanpics[-(lives + 1)])

if "_" not in place_holder:
    print("Congratz You Win !!!")

else:
    print("""It's ok better luck next time""")
    print(f"The correct word is {chosen_word}")

# import random
# from hangman_art import hangmanpics
# from hangman_words import word_list
#
# print("Find The Character")
#
# # Select a random word from the list
# chosen_word = random.choice(word_list)
# print(chosen_word)  # For testing purposes
#
# # Initialize placeholders for the word
# place_holder = ["_" for _ in range(len(chosen_word))]
# print(place_holder)
#
# # Set the maximum number of wrong guesses
# lives = 6
#
# # Loop until lives run out or the word is guessed
# while lives > 0 and "_" in place_holder:
#     guess = input("Enter a letter: ").upper()
#
#     # Check if the letter has already been guessed
#     if guess in place_holder:
#         print("Already guessed!")
#         continue
#
#     correct_guess = False
#     for index, letter in enumerate(chosen_word):
#         if guess == letter:
#             place_holder[index] = letter
#             correct_guess = True
#
#     if correct_guess:
#         print(f"Correct guess! You have {lives} lives left.")
#     else:
#         lives -= 1
#         print(f"Wrong guess. You have {lives} lives left.")
#
#     print(place_holder)
#     print(hangmanpics[-(lives + 1)])
#
# if "_" not in place_holder:
#     print("Congratulations! You win!")
# else:
#     print("It's okay. Better luck next time.")
#     print(f"The correct word was: {chosen_word}")
