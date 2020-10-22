import random

suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

deck = []

for suit in suits:
    for card in cards:
        deck.append(f'{card} of {suit}')

values = dict(zip(cards, nums))
values.update(({'1': 10}))
del values['10']

hand = []
first_deal = random.choices(deck, k=2)
hand.append(first_deal[0])
hand.append(first_deal[1])

deck.remove(first_deal[0])
deck.remove(first_deal[1])
print(f'Your hand: {hand}')

def total_value(x):
    total = 0
    card_values = []
    for card in x:
        total += values[card[0]]
        card_values.append(card[0])
    if total <= 11 and 'A' in card_values:
        total += 10
    return total


dealer_hand = random.choices(deck, k=2)
dealer = [card for card in dealer_hand]

print(f'Your total value: {total_value(hand)}', '\n')
print(f"Dealer's hand: [Unknown, {dealer[1]}]")\

if total_value(hand) == 21 and total_value(dealer) != 21:
    print('Blackjack! You win!')
elif total_value(hand) == 21 and total_value(dealer) == 21:
    print("It's a draw!")
elif total_value(dealer) == 21:
    print('Dealer has blackjack, you lose!')
else:

    option = input('"Stay" or "Hit me"? ' )

    while option.lower() != 'stay':
        if option.lower() == 'hit me':
            next_card = random.choice(deck)
            deck.remove(next_card)
            hand.append(next_card)
            print(hand)
            print(f'Total value: {total_value(hand)}')
            if total_value(hand) > 21:
                print('BUST! You lose!')
                break
            option = input('"Stay" or "Hit me"? ' )

        elif option.lower() != 'hit me' and option.lower() != 'stay':
            print('Type "Stay" or "Hit me"' )
            option = input()

    if total_value(hand) > 21:
        pass
    else:
        print(f'Final hand: {hand}')
        print(f'Final value: {total_value(hand)}\n')

        print(f"Dealer's hand: {dealer}")
        print(f"Dealer's value: {total_value(dealer)}\n")

        while total_value(dealer) < 17:
            next_card = random.choice(deck)
            deck.remove(next_card)
            dealer.append(next_card)
            print('Dealer takes a card')
            print(f"Dealer's hand: {dealer}")
            print(f"Dealer's value: {total_value(dealer)}\n")
        
        if total_value(dealer) <=21:
            print('Dealer stays')
            if total_value(hand) > total_value(dealer):
                print('You win!!')
            else:
                print('You lose!')
        else:
            print('Dealer busts, you win!!!')

        

    
