from collections import namedtuple

Card = namedtuple("Card", "value suit")
SUITS = ("Spades", "Hearts", "Diamonds", "Clubs")
VALUES = tuple(range(2, 10 + 1)) + ("Jack", "Queen", "King", "Ace")


def deck_gen(jokers=True):
    if jokers:
        yield Card("Joker", None)
        yield Card("Joker", None)
    for suit in SUITS:
        for val in VALUES:
            yield Card(val, suit)


print([c for c in deck_gen()])
