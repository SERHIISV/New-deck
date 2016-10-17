#!/usr/bin/env python

import random

from app.cards import Cards
from app.card import Card


if __name__ == "__main__":
    deck = Cards()
    first = deck[4]
    deck[4] == Card(2, 'spades')
    Card(2, 'diamonds') in deck
    random.shuffle(deck)
    deck.index(Card(2, 'diamonds'))
    random.choice(deck)
    [card.__str__() for card in deck if card.rank > 5]
