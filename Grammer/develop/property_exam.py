
## propery 함수와 propery 데코레이터

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

person = Person("John" ,"Doe",25)
print(person.age)

person.age = person.age + 1
print(person.age)

class Person:
    def __init__(self, fist_name, last_name, age):
        self.first_name = fist_name
        self.last_name = last_name
        self.set_age(age)

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age

    # property(getter, setter)
    age = property(get_age, set_age)

person = Person("John", "Doe", 20)
# print(person.age)
# person.age = -1

print("="*100)

class Person:
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name =  last_name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age

person = Person("John", "Doe" , 20)
print(person.age)
# person.age = -1 -> 안됨

person.age = person.age +1
print(person.age)

