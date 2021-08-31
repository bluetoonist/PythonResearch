class MetaSingleton(type):

    def __init__(cls, *args):
        print(cls, "__init__ method called with args ", args)
        type.__init__(cls, args)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls, "creating instance args", args, kwargs)
            cls.instance = type.__call__(cls, *args, **kwargs)
        return cls.instance


def test_single(cls):
    return cls() == cls()


class SingletonM(metaclass=MetaSingleton):
    def __init__(self):
        self.a = 1


if __name__ == '__main__':
    instance1 = SingletonM()
    print(instance1.a)
