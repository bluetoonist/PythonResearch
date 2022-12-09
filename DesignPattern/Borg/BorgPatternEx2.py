class Borg(object):
    """ 싱글톤이 아님 """
    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data


class ABorg(Borg):
    pass


class BBorg(Borg):
    pass


class A1Borg(Borg):
    pass


if __name__ == '__main__':
    a = ABorg()
    a1 = A1Borg()
    b = BBorg()

    a.x = 100  # Borg를 상속받은 a instance 에만 속성을 할당함

    print(a.x)
    # a1 과 b 에서 같이 사용할 수 있음
    # Why?
    # 같은 상태를 공유하는 Borg를 상속받았기 때문임
    print(a1.x)
    print(b.x)
