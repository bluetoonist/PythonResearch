import copy


class MetaPrototype(type):

    def __init__(cls, *args):
        type.__init__(cls, *args)
        cls.clone = lambda self: copy.deepcopy(self)


class PrototypeM(metaclass=MetaPrototype):
    pass


class ItemCollection(PrototypeM):
    """ An Item collection class """

    def __init__(self, items=[]):
        self.items = items


if __name__ == '__main__':
    i1 = ItemCollection(items=['apples', 'grapes', 'oranges'])
    print(i1)

    i2 = i1.clone()
    print(i2) # 복제본은 다른 객체이다
    
