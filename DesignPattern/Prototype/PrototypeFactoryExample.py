import copy


class Borg(object):
    """ 싱글톤이 아님 """
    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data


class PrototypeFactory(Borg):
    """ A Prototype factory/registry class """

    def __init__(self):
        super().__init__()
        self._registry = {}

    def register(self, instance):
        self._registry[instance.__class__] = instance

    def clone(self, klass):

        instance = self._registry.get(klass)

        if instance is None:
            print("Error: ", klass, "not registerd")
        else:
            return instance.clone()


class SPrototype(object):
    """ A prototype base class using shallow copy """

    def clone(self):
        """ Return a Clone of self """
        return copy.copy(self)


class Name(SPrototype):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return ''.join((self.first, self.second))


class Animal(SPrototype):
    def __init__(self, name, type="Wild"):
        self.name = name
        self.type = type

    def __str__(self):
        return ''.join((str(self.type), self.name))


if __name__ == '__main__':
    name = Name('Bill', 'Bryson')
    animal = Animal('Elephant')

    print(name)

    print(animal)

    factory = PrototypeFactory()
    factory.register(name)
    factory.register(animal)

    factory.clone(Name)

    factory.clone(Animal)


    class C(object): pass


    factory.clone(C)

    from enum import Enum