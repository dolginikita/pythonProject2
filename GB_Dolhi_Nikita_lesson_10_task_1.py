from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expenditure(self):
        pass


class Coat(Clothing):
    @property
    def expenditure(self):
        return self.param / 6.5 + 0.5


class Suit(Clothing):
    @property
    def expenditure(self):
        return self.param * 2 + 0.3


coat = Coat(54)
suit = Suit(1.8)
print(coat.expenditure)
print(suit.expenditure)