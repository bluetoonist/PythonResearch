# Polymorphism 다형성
"""
    같은 모양의 코드가 다른 동작을 하는 것

    *다형성은 코드의 양을 줄이고, 여러 객체 타입을 하나의 타입으로
        관리가 가능하며 유지보수에 좋음

"""


# Member Override( 메서드 재정의) - 다형성의 한 예

class Person:
    def __init__(self,name):
        self.name = name

    def work(self):
        print(self.name +" works Hard")

class Student(Person):
    def work(self):
        print(self.name +" Studies hard")

class Engineer(Person):
    def work(self):
        print(self.name +"deverlops someting")

student1 = Student("Dave")
deverloper1 = Engineer("David")

student1.work()
deverloper1.work()

# 메서드명을 동일하게 해서 같은 모양의 코드가 다른 동작을 하도록 함
print("==========="*5)
class SalesWorker:
    def __init__(self,name):
        self.name = name
    def work(self):
        return self.name+" Sells Something"

class DevWorker:
    def __init__(self,name):
        self.name = name
    def work(self):
        return  self.name+" Develops Something"

list1 = ['Dave','David','Andy','Aiden','Tina','Anthony']

dic1 = {}


for i,li in zip(range(1,7),list1):
    dic1["worker"+str(i)] = SalesWorker(li)
    if i > 3:
        dic1["worker"+str(i)] = DevWorker(li)


for j in range(1,7):
 print(dic1["worker"+str(j)].work())
