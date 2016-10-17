#!/usr/bin/env python
import random
import itertools

from card import Card


class Cards(object):
    ranks = range(1, 14)
    suits = ['spades', 'hearts', 'clubs', 'diamonds']

    def __init__(self):
        self.deck = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __getitem__(self, key):
        return self.deck[key]

    def __contains__(self, some_card):
        if some_card in self.deck:
            return True
        else:
            return False

    def __len__(self):
        return len(self.deck)

    def __setitem__(self, k, value):
        self.deck[k] = value
        return self

    def __repr__(self):
        new_deck = " ".join([str(card) for card in self.deck])
        return new_deck

    def get_cards(self):
        cards = [card for card in self.deck if card.rank > 5]
        return cards

    def index(self, card):
        return self.deck.index(card)
