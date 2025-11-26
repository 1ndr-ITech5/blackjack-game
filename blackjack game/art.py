import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/           
"""


def player_turn(user_pack, user_score, comp_card):
    while True:
        print(f"Your cards: {user_pack}, current score: {user_score}")
        print(f"Computer's first card: {comp_card}")

        draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_card == "y":
            new_card = random.choice(cards)
            user_pack.append(new_card)

            from functions import ace
            user_score = ace(user_score, user_pack)

            if user_score > 21:
                print(f"Your final hand: {user_pack}, final score: {user_score}")
                return user_score, False

        else:
            return user_score, False


def computer_turn(comp_score, comp_deck):
    while comp_score < 17:

        comp_new_card = random.choice(cards)
        comp_deck.append(comp_new_card)
        
        from functions import ace
        comp_score = ace(comp_score, comp_deck)

    print(f"Computer's final hand: {comp_deck}, final score: {comp_score}")
    return comp_score, False