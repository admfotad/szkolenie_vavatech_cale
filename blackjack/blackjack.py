


def display_table(dealer_cards, player_cards):
    print("Dealer:")
    print(dealer_cards)
    print("Player:")
    print(player_cards)


if __name__ == '__main__':
    player = Player(1000)
    while player.money > 0:
        print('Your money: ${}'.format(player.money))
        while True:
            bet_string = input('Your bet: ')
            try:
                bet = int(bet_string)
            except ValueError:
                print('bed value')
                continue
            if bet > player.money:
                print('Insufficient money')
                continue
            break

        deck = shuffle_deck()
        player.cards = Hand([])
        dealer_cards = Hand([])
        for i in range(2):
            player.cards.add_card(deck.pop())
        dealer_cards.add_card(deck.pop())
        display_table(dealer_cards, player.cards)
        while True:
            while True:
                action = input('Do you (h)it, (s)tand or (d)ouble down?')
                if action not in ['h', 's', 'd']:
                    continue
                break
            if action == 'h':
                player.cards.add_card(deck.pop())
                display_table(dealer_cards, player.cards)
                if player.cards.bust:
                    break
            elif action == 'd':
                if bet <= player.money // 2:
                    bet *= 2
                    player.cards.add_card(deck.pop())
                    break
                else:
                    print('Insufficient money')
                    continue
            elif action == 's':
                break
        if player.cards.bust:
            print('You bust!')
            player.money -= bet
            continue
        while (
            dealer_cards.value < 16 or
            dealer_cards.value == 17 and dealer_cards.soft
        ):
            dealer_cards.add_card(deck.pop())
        display_table(dealer_cards, player.cards)
        if player.cards.blackjack:
            print('Blackjack')
            player.money += round(bet * 1.5)
        elif dealer_cards.bust:
            print('Dealer busts')
            player.money += bet
        elif dealer_cards.value == player.cards.value:
            print('Push')
        elif dealer_cards.value > player.cards.value:
            print('Dealer wins')
            player.money -= bet
        else:
            print('Player wins')
            player.money += bet
    print("You're bankrupt")
