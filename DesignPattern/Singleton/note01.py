class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


def test_singleton(cls):
    print(type(Singleton()), type(cls))
    return type(Singleton) == type(cls)


class SingleTonA(Singleton):
    def __init__(self):
        pass


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    print(hex(id(s1)))
    print(hex(id(s1)))

    print(s1 == s2)

    a = SingleTonA()

    print(test_singleton(a))
