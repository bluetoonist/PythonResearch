class Singleton(object):
    """ Singleton in Python """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            # 가장 처음 생성된 instance에 class 주소 할당시킴
            # 이후 생성된 _instance는 고정된 값을 가지게 됨
            cls._instance = object.__new__(cls)
        return cls._instance


class SingletonA(Singleton):
    pass


class SingletonB(object):
    pass


if __name__ == '__main__':
    def test_single(cls):
        print(cls(), cls())
        return cls() == cls()  # 같은 클래스를  두 번 호출해서 클래스의 주소를 비교함


    print("Sington : ", hex(id(Singleton)))
    print("SingtonA : ", hex(id(SingletonA)))

    print("====================================")
    s1 = Singleton()
    s2 = Singleton()

    print("====================================")
    print(id(s1), id(s2))
    print(s1 == s2)

    print("====================================")
    print(test_single(SingletonA))
    print(test_single(SingletonB))
