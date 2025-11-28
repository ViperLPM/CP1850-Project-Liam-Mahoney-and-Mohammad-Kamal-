import db
import random

#imported the read and write txt functions on db.py
#prototype idea of dealer's show card for the time being
#switching the suit, rank and point_value arg to main
def create_deck_list(suit, rank, point_value):
    """suit_choice=random.choice(suit)
    rank_choice=random.choice(rank)
    print(f"{rank_choice} of {suit_choice}")"""
    deck=[]
    for suits in suit:
        for i, ranks in enumerate(rank):
            point=point_value[i]
            card=[suits, ranks, point]
            deck.append(card)
    return deck

def draw_card(deck):
    hand= random.choice(deck)
    deck.remove(hand)
    return hand

def get_hand_points(hand):
    points= 0
    num_aces = 0

    for card in hand:
        point = card[2]
        points += point

        if point == 11:
            num_aces += 1

    while points > 21 and  num_aces >0: #trynna change the ace points from 11-1
        points -= 10
        num_aces-= 1
    return points


def main():
    print("BLACKJACK")
    print("Blackjack payout is 3:2")
    suit= ["Hearts", "Diamonds", "Clubs", "Spades"]
    rank=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    point_value=[2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    full_deck=create_deck_list(suit,rank,point_value)
    #checking the amount of cards because getting confused if its drawing correctly or not
    print(f"initial size of deck: {len(full_deck)} ")
    test_draw=draw_card(full_deck)
    print(f"Card drawn: {test_draw}")
    print(f"New deck size:{len(full_deck)}")
    #testing with a single drawn card
    single_card_hand= [test_draw]
    card_points=get_hand_points(single_card_hand)
    print(f"points for the drawn card is: {card_points}")


if __name__=="__main__":
    main()










