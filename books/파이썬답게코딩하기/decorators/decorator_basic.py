from typing import Callable


def deco(func: Callable):

    def wrapper():
        print("before")
        ret = func()
        print("after")
        return ret

    return wrapper


@deco
def base():
    print("base function")


if __name__ == '__main__':
    print("=== Run Decorator ===")
    base()
