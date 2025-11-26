import os
import random
from art import cards, logo, player_turn, computer_turn
from functions import player_blackjack, comp_blackjack, player_busts, comp_busts, point_checker

game_on = True

balance = 1000

while game_on:

    user_choice = input("Type 'y' to play Blackjack or 'n' to exit: ").lower().strip()

    if user_choice == "y":
        os.system("cls")
        print(f"\n{logo}")
        
        go = True
        while go:
            bet = int(input(f"\nYou have ${balance}. How much would you like to bet? $"))
            if bet > balance:
                print("You cannot bet a larger amount that the current balance!")
            elif bet < 0:
                print("The bet cannot be a negative amount!")
            else:
                go = False

        balance -= bet

        card1 = random.choice(cards)
        card2 = random.choice(cards)

        user_pack = [card1, card2]
        user_score = sum(user_pack)

        comp_card = random.choice(cards)
        comp_deck = [comp_card]
        comp_score = comp_card

        player_round = True
        should_comp_play = True

        while player_round:
            user_score, player_round = player_turn(user_pack, user_score, comp_card)
            if player_blackjack(user_score, user_pack):
                result = "win"
                print("Win with a Blackjack 😎")
                balance += bet * 2.5
                should_comp_play = False

            elif player_busts(user_score):
                result = "lose"
                print("You went over. You lose 😭")
                should_comp_play = False


        if should_comp_play:
            comp_round = True 
            while comp_round and user_score <= 21:
                comp_score, comp_round  = computer_turn(comp_score, comp_deck)
                if comp_blackjack(comp_score, comp_deck):
                    result = "lose"
                    print("You lost by a blackjack from computer!")
                elif comp_busts(comp_score):
                    result = "win"
                    print("Opponent went over. You win 😁")
                    balance += bet * 2


            result = point_checker(user_score, comp_score)
            if result == "You win 😃":
                balance += bet * 2
            elif result == "Draw 🙃":
                balance += bet

        print(result)

        print(f"Your current balance: ${balance}")

        if balance == 0:
            print("Oops! Balance is dead drought. Game Over!!")
            game_on = False

    else:
        print(f"Thanks for playing! Your final balance: ${balance}")
        game_on = False