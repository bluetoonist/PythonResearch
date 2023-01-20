import abc


class ISample(abc.ABC):

    @abc.abstractmethod
    def method(self): ...


class SubSample:

    def method01(self):
        return "String"


if __name__ == '__main__':
    ISample.register(SubSample)

    s = SubSample()

    print(s.method01())