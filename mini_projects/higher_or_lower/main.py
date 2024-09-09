import random
from data import data
from mini_projects.higher_or_lower.art import vs_art, high_low_art


def play_game():
    #print the art
    print(high_low_art)
    #compare which is higher
    # def compare(get_a, get_b, chosen_word):
    #
    #     if chosen_word == 'A' and get_a > get_b:
    #         return True
    #     elif chosen_word == 'B' and get_a > get_b:
    #         return False
    #     elif chosen_word == 'A' and get_a < get_b:
    #         return False
    #     elif chosen_word == 'B' and get_a < get_b:
    #         return True
    #     else:
    #         print("False")

    def compare(get_a, get_b, chosen_word):
        if chosen_word == 'A':
            return get_a > get_b
        elif chosen_word == 'B':
            return get_b > get_a
        else:
            return False

    score = 0
    play = True
    while play:
        #pick a dict randomly from the list
        pick_a = random.randint(0, len(data) - 1)
        opt_a_name = data[pick_a]['name']
        opt_a_description = data[pick_a]['description']
        opt_a_country = data[pick_a]['country']
        opt_a_value = data[pick_a]['value']

        print(f"Name: {opt_a_name}")
        print(f"Description: {opt_a_description}")
        print(f"Country: {opt_a_country}")

        #print vs art
        #print("\n")
        print(vs_art)
        #print("\n")

        # Pick a 2nd dict from the list, ensuring it's different from the first
        pick_b = random.randint(0, len(data) - 1)
        while pick_b == pick_a:
            pick_b = random.randint(0, len(data) - 1)
        opt_b_name = data[pick_b]['name']
        opt_b_description = data[pick_b]['description']
        opt_b_country = data[pick_b]['country']
        opt_b_value = data[pick_b]['value']

        print(opt_b_name)
        print(opt_b_description)
        print(opt_b_country)

        #ask the user to select  an option
        user_choice = input("A or B which one will be higher: ").upper()

        play = compare(opt_a_value,opt_b_value,user_choice)
        print(play)

        if play:
            score += 1
            print(f"score: {score}")
        else:
            print(f"score: {score}")
            print("Game Over!!!!")

            should_continue = input("Type 'Y' to continue or 'N' to quit: ").upper()
            while should_continue not in ['Y', 'N']:
                should_continue = input("Invalid choice. Type 'Y' to continue or 'N' to quit: ").upper()
            if should_continue == 'N':
                play = False
            else:
                play = True
play_game()
