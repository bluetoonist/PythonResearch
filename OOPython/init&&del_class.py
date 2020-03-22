# class 생성자와 소멸자
#  __init__ 생성자
#  __del__ 소멸자

class Quardrangle:
    width = 0
    height =0;
    color = 'black'

sqaure = Quardrangle()

print(sqaure.width,sqaure.height,sqaure.color)

class Quardrangle:
    def __init__(self,width,height,color):
        self.width = width
        self.height = height
        self.color = color

sqaure = Quardrangle(5,5,'black')
print(sqaure.width,sqaure.height,sqaure.color)

class Quardrangle:
    def __init__(self,width,height,color):
        self.width = width
        self.height = height
        self.color = color
    def __del__(self):
        print("Quardrangle object is deleted")
sqaure = Quardrangle(5,5,'black')

import math

class Quardrangle:
    def __init__(self,length):
        self.length = length
    def get_area(self):
        return (math.sqrt(3)/2) * self.length**2

sqaure = Quardrangle(10)
print(sqaure.get_area())