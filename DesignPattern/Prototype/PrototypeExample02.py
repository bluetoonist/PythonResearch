# Shallow Copy

import copy


class SPrototype(object):
    """ A prototype base class using shallow copy """

    def clone(self):
        """ Return a Clone of self """
        return copy.copy(self)


class SRegister(SPrototype):
    """ Sub-Class of SPrototype """

    def __init__(self, names=[]):
        self.names = names


if __name__ == '__main__':
    r1 = SRegister(names=['amy', 'stu', 'jack'])
    r2 = r1.clone()

    # r1에 names에 추가
    r1.names.append('bob')

    # r2에 데이터 확인
    print(r2.names)

    # 얕은 복사로 인해 참조만 복사하고 r1과 r2는 같은 names 리스트를 공유
    print(r1.names is r2.names)

    
