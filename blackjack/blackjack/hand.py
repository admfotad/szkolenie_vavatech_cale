import random

import termcolor


SUITS = {
        'S': ('\u2660', 'red'),
        'H': ('\u2661', 'red'),
        'D': ('\u2662', 'red'),
        'C': ('\u2663', 'red'),
}


class Card():
    'A single card'

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        suit, color = SUITS[self.suit]

        return termcolor.colored(self.rank + suit, color, 'on_grey')

    __repr__ = __str__

    def get_value(self, current):
        if self.rank == 'A':
            if current > 10:
                return 1, False
            else:
                return 11, True
        elif self.rank in 'TJQK':
            return 10, False
        else:
            return int(self.rank), False

    def get_order(self):
        result = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 11,
            'T': 10,
        }.get(self.rank)
        return (result or int(self.rank)), False

    def __lt__(self, other):
        return self.get_order() < other.get_order()


class Hand():
    """A hand consisting of several cards"""
    def __init__(self, cards):
        self._cards = cards
        self._calculate()

    def __str__(self):
        result = []
        for card in self._cards:
            result.append(str(card))
        result = ','.join(result)
        if self.blackjack:
            special = ' Blackjack!'
        elif self.bust:
            special = ' Bust!'
        else:
            special = ''
        if self.soft:
            soft = 'soft'
        else:
            soft = ''
        result += '\n{}{}{}'.format(soft, self.value, special)
        return result

    def _calculate(self):
        self.value = 0
        self.soft = False
        for card in sorted(self._cards):
            value, is_soft = card.get_value(self.value)
            self.value += value
            if is_soft:
                self.soft = True
        self.blackjack = len(self._cards) == 2 and self.value == 21
        self.bust = self.value > 21

    def add_card(self, card):
        """Adds a card to the hand"""
        self._cards.append(card)
        self._calculate()


class Player():
    def __init__(self, money):
        self.money = money


def shuffle_deck():
    cards = []
    for rank in 'AKQJT98765432':
        for suit in 'SHDC':
            cards.append(Card(rank, suit))
    random.shuffle(cards)
    return cards
