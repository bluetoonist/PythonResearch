class Borg(object):
    """ 싱글톤이 아님 """
    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data


class IBorg(Borg):

    # Borg를 이용해 인스턴스가 동일하지 않더라도 같은 상태를 공유하는
    # 인스턴스를 갖는 클래스를 생성함

    def __init__(self):
        Borg.__init__(self)
        self.state = "init"

    def __str__(self):
        return self.state


if __name__ == '__main__':
    i1 = IBorg()
    i2 = IBorg()

    print(i1)
    print(i2)

    i1.state = "running"  # i1에서 상태값을 바꾸면

    print(i1.state)
    print(i2.state)  # i2의 상태도 바뀜

    print(i1 == i2)
