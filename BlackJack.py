import random
import time


# shuffles the deck - 52 cards
def shuffle():
    cards = (['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])*4
    random.shuffle(cards)
    return cards


# removes a card from the deck and deals it to the player
def deal(card_deck, player):
    card = card_deck.pop()
    player.append(card)


# checks the hand value
def total(dealt_cards):
    cards = []
    aces = 0
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    for card in dealt_cards:
        cards.append(values[card])
        if card == 'A':  # ace can be both 1 and 11
            aces += 1
    hand_value = sum(cards)
    # if hand value exceeds 21 and the player has aces, take ace as 1
    while hand_value > 21 and aces > 0:
        hand_value = hand_value - 10
        aces = aces - 1
    return hand_value


# if no one busts(exceeds 21) - compare hand values to determine winner
def compare(player, dealer):
    if total(player) > total(dealer):
        print("You win")
    elif total(dealer) > total(player):
        print("Dealer wins")
    else:
        print("It's a tie")


# main game
def blackjack():
    deck = shuffle()
    player_cards = []
    dealer_cards = []
    for i in range(2):
        deal(deck, player_cards)
        deal(deck, dealer_cards)

    # One card of dealer is hidden
    hidden_card = dealer_cards[1]
    dealer_cards[1] = 'X'
    print("\nDealing...")
    time.sleep(2)
    print("You:", player_cards, " Total:", total(player_cards))
    print("Dealer:", dealer_cards)

    # If blackjack (player)
    if total(player_cards) == 21:
        print("Blackjack! You win")
        return

    # Player chance
    choice = input("Do you want to hit(h) or stand(s)? : ")
    # If 'h' is not entered, player automatically stands and the game continues
    # Should probably add a way for the user to correct themselves here
    while choice.lower() == 'h':
        deal(deck, player_cards)
        print("You hit...")
        time.sleep(1)
        print("You:", player_cards, " Total:", total(player_cards))
        time.sleep(1)

        if total(player_cards) > 21:  # hand value exceeds 21
            print("You bust! Dealer wins")
            return
        choice = input("Do you want to hit(h) or stand(s)?: ")

    # Reveal dealer card
    dealer_cards[1] = hidden_card
    print("Dealer:", dealer_cards, " Total:", total(dealer_cards))

    # If blackjack (dealer)
    if total(dealer_cards) == 21:
        print("Blackjack! Dealer wins")
        return

    # Deal cards to the dealer while sum < 17
    while total(dealer_cards) < 17:
        deal(deck, dealer_cards)
        print("Dealer hits...")
        time.sleep(1)
        print("Dealer:", dealer_cards, " Total:", total(dealer_cards))
        time.sleep(1)
        if total(dealer_cards) > 21:  # hand value exceeds 21
            print("Dealer bust! You win")
            return

    # Compare cards and print winner
    time.sleep(1)
    compare(player_cards, dealer_cards)


print("Welcome! Let's play BlackJack")
answer = True
while answer:
    blackjack()
    playing = input("\nDo you want to continue playing? (y/n): ")
    # If 'y' is not entered, the game automatically ends
    # Should probably add a way for the user to correct themselves here
    if playing.lower() != 'y':
        answer = False
        print("\nBye! Thanks for playing")
        time.sleep(2)

# Future Plans:
# 1) Score/wins tracker or money (virtual) tracker - a ledger, user can bet custom amounts and win/lose accordingly
# 2) A multiplayer option where more than 1 user can play against the dealer
# 3) Graphical user interface and possibly host on a server
# 4) More real-game options like split, insure
