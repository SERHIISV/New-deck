#!/usr/bin/env python
class Card(object):
    ranks = range(1, 14)

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __lt__(self, other):
        return self.value() < other.value()

    def __le__(self, other):
        return self.value() <= other.value()

    def __eq__(self, other):
        return self.value() == other.value()

    def __ne__(self, other):
        return self.value() != other.value()

    def __gt__(self, other):
        return self.value() > other.value()

    def __ge__(self, other):
        return self.value() >= other.value()

    def __str__(self):
        return "%s %s" % (self.rank, self.suit)

    def value(self):
        return self.ranks.index(self.rank)
