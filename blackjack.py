import db
import random

def create_deck_list(suit, rank, point_value):
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


def initialize_money(start_amount=100.00):
    file_name= db.FILENAME
    try:
        money= db.read_money()
        return money
    except FileNotFoundError:
        print(f"File {file_name} not found. Initializing money to {start_amount}." )
        db.write_money(str(start_amount))
        return start_amount
    except ValueError:
        print(f"Error reading {file_name} as it is invalid. Initialize money to {start_amount}.")
        db.write_money(str(start_amount))
        return start_amount

def validate_bet_amount(money_amount):
    min_amount = 5
    while money_amount < min_amount:
        print(f"Current money ({money_amount}) is less than {min_amount}")
        choice = input("Would you like to buy chips? (y/n)")
        if choice.lower() == "y":
            purchase_amount = 100
            money_amount += purchase_amount
            db.write_money(str(money_amount))
            print(f"You purchased {purchase_amount}, your current balance is now {money_amount}")
            break
        elif choice.lower() == "n":
            print("You can no longer place a minimum bet.")
            return None
        else:
            print("invalid input, enter either y or n")
    return money_amount

def get_bet(money_amount):
    min_bet= 5
    max_bet = 1000
    while True:
        bet_input = input(f"Bet amount (minimum{min_bet} to max{max_bet}):   ")
        try:
            bet= float(bet_input)
        except ValueError:
            print("Please enter a valid integer or a float value for bet amount")
            continue

        if bet < min_bet:
            print(f"The minimum bet should be {min_bet}")
            continue
        if bet > max_bet:
            print(f"The maximum bet should be {max_bet}")
            continue
        if bet > money_amount:
            print(f"The bet cannot be bigger than the player's current money{money_amount} amount")
            continue

        return bet


def dealer_turn(dealer_hand, full_deck):
    for card in dealer_hand:
        print(f"{card[1]} of {card[0]}")

    while get_hand_points(dealer_hand) < 17:
        new_card= draw_card(full_deck)
        dealer_hand.append(new_card)
        print(f"DEALER'S CARDS :{new_card[1]} of {new_card[0]}")

    dealer_points= get_hand_points(dealer_hand)
    if dealer_points > 21:
        return True
    else:
        return False

def player_turn(player_hand, full_deck):
    while True:
        player_points =get_hand_points(player_hand)
        if player_points > 21:
            return True
        elif player_points ==21:
            return False
        choice= input ("Hit or stand? (hit/stand):  ").lower()
        if choice == "stand":
            return False
        elif choice == "hit":
            new_card= draw_card(full_deck)
            player_hand.append(new_card)

            print("\nYOUR CARDS:")
            for card in player_hand:
                print(f"{card[1]} of {card[0]}")
        else:
            print("Please type 'hit or 'stand' ")




def main():
    print("BLACKJACK")
    print("Blackjack payout is 3:2")
    money_amount= db.read_money()
    money_amount= validate_bet_amount(money_amount)
    print(f"Money:  {money_amount}")
    player_bet=get_bet(money_amount)
    print(f"Bet amount: {player_bet}")
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
    """player_test_hand= []
    first_card = draw_card(full_deck)
    player_test_hand.append(first_card)

    second_card = draw_card(full_deck)
    player_test_hand.append(second_card)

    player_turn(player_test_hand, full_deck)
    
    tested player_turn()"""
    







if __name__=="__main__":
    main()










