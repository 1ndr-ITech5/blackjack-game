def player_blackjack(user_score, user_pack):
    return user_score == 21 and len(user_pack) == 2
    

def comp_blackjack(comp_score, comp_deck):
    return comp_score == 21 and len(comp_deck) == 2


def player_busts(user_score):
    return user_score > 21
    
    
def comp_busts(comp_score):
    return comp_score > 21


def ace(score, hand):
    score = sum(hand)
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score -= 10
        score = sum(hand)
        
    return score
    

def point_checker(user_score, comp_score):
    if comp_score > user_score and comp_score <= 21:
        return "You lose 😤"

    elif comp_score == user_score:
        return "Draw 🙃"

    elif user_score > comp_score and user_score <= 21:
        return "You win 😃"