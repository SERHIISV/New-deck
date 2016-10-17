#!/usr/bin/env python
import sys
sys.path.append("..")

from random import shuffle, choice

from new_deck.app import cards, card


class Actions:
    """
    Class Actions is a controller of actions

    Available methods:
        - show_hand()
        - show_deck()
        - choose_card()
        - choose_by_index()
        - determine()
        - random_choose()
        - shuffle_deck()
        - compare()
        - sort_by_rank()
        - sort_by_suit()
        - drop_cards()
    """
    def __init__(self):
        self.deck = cards.Cards()

    def shuffle_deck(self, deck):
        """
        Shuffles cards in the deck randomly
        """
        shuffle(deck)
        return deck

    def choice_by_index(self, index):
        """
        Choosing a card by index
        """
        try:
            index = int(index)
            return "Card(rank='%s', suit='%s')" % (self.self.deck[index-1][0], self.self.deck[index-1][1])
        except ValueError:
            print "That is not a number."
            self.choose_by_index()

    def exist_card(self, card):
        """
        Determining current place of card in the deck.
        :param index: determined index of card in hand
        """

        if card in self.deck:
            return "Card(rank='%s', suit='%s') is exist" % (card[0], card[1])
        else:
            return "Card(rank='%s', suit='%s') does not exist" % (card[0], card[1])

    def rand_choice(self):
        """
        Randomly choosing of a card
        """
        card = choice(self.deck.deck)
        return "Card(rank='%s', suit='%s') does not exist" % (card[0], card[1])

    def compare(self):
        """
        comparing two cards by waight
        """


    def get_cards_with_rank(self, deck):
        """
        getting cards which has rank more than 5
        """
        cards = [card for card in self.deck.deck if card.rank > value]
        return cards
