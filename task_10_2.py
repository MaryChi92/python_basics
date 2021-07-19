from abc import abstractmethod


class Clothes:
    total_fabric = 0

    def __init__(self, v=0, h=0):
        self.v = v
        self.h = h

    @abstractmethod
    def fabric_quantity(self):
        pass


class Coat(Clothes):

    @property
    def fabric_quantity(self):
        quantity = round((self.v / 6.5 + 0.5), 2)
        Clothes.total_fabric += quantity
        return quantity


class Suit(Clothes):

    @property
    def fabric_quantity(self):
        quantity = 2 * self.h + 0.3
        Clothes.total_fabric += quantity
        return quantity


coat1 = Coat(36)
print(coat1.fabric_quantity)

suit1 = Suit(h=167)
print(suit1.fabric_quantity)

print(Clothes.total_fabric)
