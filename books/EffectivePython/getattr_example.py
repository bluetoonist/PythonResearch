class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = "Value for %s" % name
        setattr(self, name, value)
        return value


data = LazyDB()
print("Before :", data.__dict__)
print("foo  :", data.foo)
print("After :", data.__dict__)

print("=" * 100)


class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print("Called __getattr__(%s)" % name)
        return super().__getattr__(name)


data = LoggingLazyDB()
print("exists:", data.exists)
print("foo: ", data.foo)
print("foo: ", data.foo)

# hasattr로 프로퍼티가 있는지 확인
# getattr로 프로퍼티 값을 가져옴

print("=" * 100)
data = LoggingLazyDB()
print("Before : ", data.__dict__)
print("foo exists : ",hasattr(data,"foo"))
print("After : ", data.__dict__)
print("foo exists", hasattr(data, "foo"))