class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def display(self):
        print(f"Your card is {self.value} of {self.suit}")

def ask_input():
    value = input("Please enter a value: ").upper()
    suit = input("Please enter a suit: ").upper()
    return  value, suit

value, suit = ask_input()
card1 = Card(value, suit)
card1.display()
