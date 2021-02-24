class Number:
    def __init__(self, value):
        self.value = value

    def __It__(self, other):
        return self.value < other.value

    def __Ie__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value
        