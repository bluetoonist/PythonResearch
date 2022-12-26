import rx

observable = rx.of(1, 2, 3)


def hanlder(arg):
    print(arg)


observable.subscribe(hanlder)
