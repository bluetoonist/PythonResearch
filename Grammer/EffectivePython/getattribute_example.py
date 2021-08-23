"""
@ TOPIC : __getarttribute__
@ DESCRIPTOR
  객체의 속성에 접근할 떄마다 호출되며,
  해당 속성이 속성 딕셔너리에 있을 떄도 호출,
  속성에 접근할 떄마다 전역 트랜잭션 상태를 확인하는 작업 등에 쓸 수 있음.

"""


class ValidationDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print("Called __getattribute__(%s)" % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = "Value for %s" % name
            setattr(self, name, value)
            return value


data = ValidationDB()
print("exists: ", data.exists)
print("foo: ", data.foo)
print("foo: ", data.foo)


# 동적으로 접근한 프로퍼티가 존재하지 않아야 하는 경우에 AttributeError를 일으킴
class MissingPropertyDB(object):
    def __getattr__(self, name):
        if name == "bad_name":
            raise AttributeError("%s is missing " % name)


data = MissingPropertyDB()
data.bad_name


