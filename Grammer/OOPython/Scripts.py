class Symbol(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        else:
            return NotImplementedError

    def __hash__(self):
        print(hash(self.value))
        return hash(self.value)


if __name__ == "__main__":
    x = Symbol("Py")
    y = Symbol("Py")

    symbols = set()
    symbols.add(x)
    symbols.add(y)

    print(x is y) # Object Compare
    print(x == y) # Value Compare
    print(len(symbols))
