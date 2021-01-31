

class sample:
    def __init__(self,x):
        self.x = x

# getattr
c = sample(1)
print(getattr(c, 'x'))

c = sample(2)

# setattr
setattr(c,'y',2)


print(c.__dir__())

