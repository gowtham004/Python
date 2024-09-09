import random
from data import data
from mini_projects.higher_or_lower.art import vs_art, high_low_art

def play_game():
    # Print the art
    print(high_low_art)

    def compare(get_a, get_b, chosen_word):
        if chosen_word == 'A':
            return get_a > get_b
        elif chosen_word == 'B':
            return get_b > get_a
        else:
            return False

    score = 0
    play = True

    # Initial pick for pick_a
    pick_a = random.randint(0, len(data) - 1)

    while play:
        opt_a_name = data[pick_a]['name']
        opt_a_description = data[pick_a]['description']
        opt_a_country = data[pick_a]['country']
        opt_a_value = data[pick_a]['value']

        print(f"Name: {opt_a_name}")
        print(f"Description: {opt_a_description}")
        print(f"Country: {opt_a_country}")

        # Print vs art
        print(vs_art)

        # Pick a 2nd dict from the list, ensuring it is different from the first
        pick_b = random.randint(0, len(data) - 1)
        while pick_b == pick_a:
            pick_b = random.randint(0, len(data) - 1)
        opt_b_name = data[pick_b]['name']
        opt_b_description = data[pick_b]['description']
        opt_b_country = data[pick_b]['country']
        opt_b_value = data[pick_b]['value']

        print(f"Name: {opt_b_name}")
        print(f"Description: {opt_b_description}")
        print(f"Country: {opt_b_country}")

        # Ask the user to select an option
        user_choice = input("A or B which one will be higher: ").upper()

        play = compare(opt_a_value, opt_b_value, user_choice)
        print(play)

        if play:
            score += 1
            print(f"Score: {score}")
            # Update pick_a to be pick_b for the next round
            pick_a = pick_b
        else:
            print(f"Score: {score}")
            print("Game Over!!!!")

            should_continue = input("Type 'Y' to continue or 'N' to quit: ").upper()
            while should_continue not in ['Y', 'N']:
                should_continue = input("Invalid choice. Type 'Y' to continue or 'N' to quit: ").upper()
            if should_continue == 'N':
                play = False
            else:
                # Reset pick_a for a new game
                pick_a = random.randint(0, len(data) - 1)
                score = 0

play_game()
