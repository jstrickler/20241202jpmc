class Card:  # inherits from 'object'
    def __init__(self, rank, suit):  #   self:Python::this:Java
        self._rank = rank
        self._suit = suit

    # def get_rank(self):
    #     return self._rank

    @property
    def rank(self):  # getter property
        return self._rank
    
    @property
    def suit(self):  # getter property
        return self._suit
    
    @suit.setter
    def suit(self, value):
        self._suit = value  # assign new value

    @suit.deleter
    def suit(self):
        print("ouch!")

    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"


c = Card("8", "Diamonds")
print(c)
print(repr(c))
print(c.rank)  # properties
print(c.suit)
c.suit = "Hearts"
print(c.suit)