# classmethod 와 staticmethod
## 파이썬에서 직접 접근할 수 있는 메소드 두 가지

class CustomClass:

    # instance method
    def add_instance_method(self, a, b):
        return a + b

    @classmethod
    def add_class_method(cls, a, b):
        return a + b

    @staticmethod
    def add_static_method(a, b):
        return a + b

# 개념상 : 첫번째 인자에 객체를 할당하고 사용해야함
print(CustomClass.add_class_method(3,5))

# 개념상 : 첫 번쨰 인자가 클래스지만 생략하고 접근 가능
print(CustomClass.add_class_method(3,5))
print(CustomClass.add_static_method(3,5))


## classmethod 와 staticmethod의 차이는?
#### 상속

class Language:
    default_language = "English"

    def __init__(self):
        self.show = "My Language Is " + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()

    def print_lanugate(self):
        return self.show

class KoreaLanguage(Language):
    default_language = "한국어"


a = KoreaLanguage.static_my_language()
b = KoreaLanguage.class_my_language()

print(a.print_lanugate())
print(b.print_lanugate())

