
class Person:
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age =age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        if age <0:
            raise ValueError("Invalid age")
        self._age = age

print("="*25)

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return self.first_name+ " " + self.last_name

person = Person("John", "Doe", 20)
print(person.full_name)