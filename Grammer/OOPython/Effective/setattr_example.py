class SavingDB(object):
    def __setattr__(self, name, value):
        super().__setattr__(name, value)


class LoggingSavingDB(SavingDB):
    def __setattr__(self, name, value):
        print("Called __setattr__(%s %r)" % (name, value))
        super().__setattr__(name, value)

data = LoggingSavingDB()
print("Before : ", data.__dict__)
data.foo = 5
print("After  : ", data.__dict__)
data.foo = 7
print("After : ", data.__dict__)