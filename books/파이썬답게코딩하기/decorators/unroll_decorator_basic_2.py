from typing import Callable


def deco(func: Callable):
    def wrapper():
        print("before")
        ret = func()
        print("after")
        return ret

    return wrapper


def base():
    print("Base function")


if __name__ == '__main__':
    print("=== Run decorator ==")

    argument = base
    f = deco(argument)
    f()
