def blackjack_hand_score(hand):
    score = 0
    As = 0
    for i in hand:
        if i in ['J','Q','K']:
            score += 10
        elif i == 'A':
            score += 11
            As += 1
        else:
            score += int(i)
    new_score = score
    while new_score > 21:
        if As == 0:
            return new_score
        new_score -= 10
        As -= 1
    return new_score


hand = ["A", "K"]
print("Hand:", hand, "hand score:", blackjack_hand_score(hand))

hand = ["A", 'A','K','K']
print("Hand:", hand, "hand score:", blackjack_hand_score(hand))

hand = ["7", "8", "9"]
print("Hand:", hand, "hand score:", blackjack_hand_score(hand))

