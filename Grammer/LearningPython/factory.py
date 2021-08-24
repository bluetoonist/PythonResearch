def factory(aClass, *pargs, **kwargs):
    return aClass(*pargs, **kwargs)


class Spam:
    def doit(self, message):
        print(message)


class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job


object1 = factory(Spam)
object2 = factory(Person, "Arthur", "King")
object3 = factory(Person, name="Beian")
