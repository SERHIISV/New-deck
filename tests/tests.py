import sys
sys.path.append("..")

import random
import unittest

import data_for_tests as data

#from . import Main
from new_deck.app.cards import Cards
from new_deck.app.card import Card


class TestMethods(unittest.TestCase):
    def setUp(self):
        deck = Cards()

    def test_deck(self):
        self.assertEqual(str(deck), data.deck)

    def test_choose_by_index(self):
        self.assertEqual(str(deck[4]), '2 spades')

    def test_choose_card(self):
        self.assertEqual(deck[4] == Card(2, 'spades'), True)

    def test_determine(self):
        self.assertEqual(deck.index(Card(2, 'spades')), 4)

    def test_random_choice(self):
        first = random.choice(deck)
        second = random.choice(deck)
        self.assertNotEqual(first, second)

    def test_exist_in(self):
        self.assertEqual(Card(2, 'diamond') in deck, True)

    def test_shuffle_deck(self):
        random.shuffle(deck)
        assert deck != data.deck

    def test_get_more_then(self):
        cards = [card.__str__() for card in deck if card.rank > 5]
        self.assertEqual(cards, data.deck_more_then)

if __name__ == '__main__':
    deck = cards.Cards()
    log_file = 'tests/log_file.txt'
    f = open(log_file, "w")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    unittest.TextTestRunner(f, verbosity=2).run(suite)
    log_file = 'log_file.txt'
    f.close()
