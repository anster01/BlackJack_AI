class Card:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "".join((self.value))
