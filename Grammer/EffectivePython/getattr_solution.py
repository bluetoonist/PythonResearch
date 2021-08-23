# Recursion depth exceeded
class BrokenDictionary(object):
    def __init__(self, data):
        self._data = {}

    def __getattribute__(self, name):
        print("Called __getattribute__(%s)" % name)
        return self._data[name]


# data = BrokenDictionary({"foo": 3})
# data.foo


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        # 인스턴스 속성 딕셔너리에서 값을 얻어옴으로써 Recursion 해결?
        data_dict = super().__getattribute__('_data')
        return data_dict[name]


# data = DictionaryDB({"foo": 3})
# print(data.foo)
