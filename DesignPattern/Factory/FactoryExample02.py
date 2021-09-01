from FactoryExample import Engineer, Accountant, Admin


class EmployeeFactory(object):
    """
      EmployeeFactory 클래스는 name 파라미터를 허용하는 단일 create 팩토리 메소드를 제공한다.
      name 파라미터는 클래스 이름과 그에 따라 생성된 인스턴스와 일치한다.

    """

    @classmethod
    def create(cls, name, *args):
        """ Factory method for creating an Employee instance """

        name = name.lower().strip()

        if name == 'engineer':
            return Engineer(*args)
        elif name == 'accountant':
            return Accountant(*args)
        elif name == 'admin':
            return Admin(*args)


if __name__ == '__main__':
    factory = EmployeeFactory()

    engineer = factory.create('engineer', 'Sam', 25, 'M')
    accountant = factory.create('accountant', 'Hema', 39, 'F')

    print(engineer)
    print(accountant)

    print(accountant.get_role())