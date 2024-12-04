from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        j = Card("**JOKER1**", "**JOKER1**")
        self._cards.append(j)
        j = Card("**JOKER2**", "**JOKER2**")
        self._cards.append(j)

j = JokerDeck()
j.shuffle()
print(j.cards)
print(j)
print(repr(j))