# 싱글톤과 프로토타입을 모두 사용하는 예제
import copy


class MetaSingletonPrototype(type):
    """ A metaclass for Singleton & Prototype patterns """

    def __init__(cls, *args):
        print(cls, "__init__ method called with ", args)
        type.__init__(cls, *args)

        cls.instance = None
        cls.clone = lambda self: copy.deepcopy(cls.instance)

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls, "creating prototypical instance", args, kwargs)
            cls.instance = type.__call__(cls, *args, **kwargs)
        return cls.instance


class PrototypeM(metaclass=MetaSingletonPrototype):
    pass


class ItemCollection(PrototypeM):
    """ An Item collection class """

    def __init__(self, items=[]):
        self.items = items


if __name__ == '__main__':
    i1 = ItemCollection(items=['apples', 'grapes', 'oranges'])

    i2 = i1.clone()
    print(i2.items is i1.items)

    i3 = ItemCollection(items=['apples', 'grapes', 'mangoes'])
    print(i3 is i1)
    print(i1.items)
    print(i3.items)
