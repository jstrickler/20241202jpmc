import random
from card import Card

class EmptyDeckError(Exception):
    pass 

class CardDeck:
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "Clubs Diamonds Hearts Spades".split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if len(self.cards) == 0:
            raise EmptyDeckError("no more cards")
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        return f"{my_type.__name__}-{len(self)}"
    
    def __repr__(self):
        my_type = type(self)
        return f"{my_type.__name__}()"
    
    @classmethod
    def get_suits(cls):
        return cls.SUITS

    @staticmethod
    def hello():
        print("Hello, world")

d1 = CardDeck()
d2 = CardDeck()
print(d1)
print(f"{d2 = }")
d1.shuffle()
print(d1.cards)
print(d1.cards[0])
print()

for i in range(5):
    card = d1.draw()
    print(card)

print(f"cards left: {len(d1)}")
print(d1)
print(repr(d1))
print(d1.get_suits())
print(CardDeck.get_suits())
CardDeck.hello()