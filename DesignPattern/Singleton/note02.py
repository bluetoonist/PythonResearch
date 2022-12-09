class Metacls(type):

    def __call__(cls, *args, **kwargs):
        print("=" * 20)
        print(cls, args, kwargs)
        # if not cls.instance:
        #     cls.instance = type.__call__(cls, *args, **kwargs)
        #     print(cls.instance)

        return 2


class Soc(metaclass=Metacls):
    def __init__(self):
        print("?")


if __name__ == '__main__':
    soc = Soc()
    print(soc)
