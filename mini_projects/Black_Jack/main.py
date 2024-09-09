import random
from art_blackjack import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(u_score, d_score):
    if u_score == d_score:
        return "Draw!!!"
    elif u_score == 0:
        return "You Win!!!"
    elif d_score == 0:
        return "You Lose!!!"
    elif u_score > 21:
        return "You lose!!! you scored more than 21"
    elif d_score > 21:
        return "You Win!!! computer scored more than 21"
    elif u_score > d_score:
        return "you win!!! your score is greater than computer"
    else:
        return "You Lose"

def play_blackjack():
    art()
    user_card = []
    dealer_card = []
    user_score = -1
    dealer_score = -1
    for _ in range(2):
        user_card.append(deal_card())
        dealer_card.append(deal_card())
    game_over = False

    while not game_over:
        user_score = calculate_score(user_card)
        dealer_score = calculate_score(dealer_card)

        print(f"Your cards: {user_card}, Your score: {user_score}")
        print(f"Computer cards: {dealer_card[0]}")  # Revealing the first card of the dealer
        print(dealer_card)  # Revealing all dealer cards
        print(dealer_score)

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_choice = input("Press 'Y' to hit or 'N' to stand: ").upper()
            if user_choice == 'Y':
                user_card.append(deal_card())
            else:
                game_over = True

        while dealer_score != 0 and dealer_score < 17:
            dealer_card.append(deal_card())
            dealer_score = calculate_score(dealer_card)

    print(f"Your final score is {user_score}\nYour hand: {user_card}")
    print(compare_score(user_score, dealer_score))

play_blackjack()
while input("Enter 'Y' to play again or 'N' to quit: ").upper() == 'Y':
    print('\n'*20)
    play_blackjack()