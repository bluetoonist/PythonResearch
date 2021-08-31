class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = object.__new__(cls)
        return cls._instance


class MetaSingleton(type):
    def __init__(cls, *args):
        print(cls, "__init method called with args", args)
        type.__init__(cls, *args)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls, "creating instance", args, kwargs)
            cls.instance = type.__call__(cls, *args, **kwargs)
        return cls.instance


class SingletonM(metaclass=MetaSingleton):
    pass


if __name__ == '__main__':
    def test_single(cls):
        return cls() == cls()


    # s1 = Singleton()
    # s2 = Singleton()
    #
    # print(s1 == s2)

    print(test_single(SingletonM))
