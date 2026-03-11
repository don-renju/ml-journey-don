import random


class Dice:
    def roll():
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


roll = Dice.roll()
print(f"The number is {roll}")
