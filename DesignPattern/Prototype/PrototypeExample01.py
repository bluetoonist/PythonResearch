import copy


class Prototype(object):
    """ A prototype base class """

    def clone(self):
        """ Return a clone of self """

        # clone 메소드는 copy 메소드를 통해 구현되며 객체를 완전히 복사하고 복제본을 반환한다.
        return copy.deepcopy(self)


class Register(Prototype):
    """ A Student Register Class """

    def __init__(self, names=[]):
        self.names = names


if __name__ == '__main__':
    r1 = Register(names=['amy', 'stu', 'jack'])
    r2 = r1.clone()

    # 아래 두 개는 같은 상태를 가짐
    print(r1)
    print(r2)
