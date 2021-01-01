"""
information Hiding
class의 attribute ,method에 대해 접근을 제어할 수 있는 기능

"""

# private -> protecetd -> public
"""
private : 해당 클래스에서만 접근 가능

protected : 해당 클래스 또는 해당 클래스를 상속받은 클래스에 대해서만
접근 가능

public : 어떤 클래스라도 접근 가능

"""
print(" === public  ! ====")
#  Public
#  Python에서의 모든 attribute, method는 기본적으로 public
#  클래스 외부에서 attribute, method 접근 가능

class Quardrangle:
    def __init__(self,width,height,color):
        self.width = width
        self.height = height
        self.color = color
    def get_area(self):
        return self.width*self.height
    def set_area(self,width,height):
        self.width = width
        self.height = height

square = Quardrangle(5,5,'black')
print(square.get_area())
print(square.width)
square.width = 10
print(square.get_area())

# Protected
# 해당 속성의 앞에 _ 를 붙여서 표시만 함
# 실제 제약되지는 않고 일종의 경고 표시로 사용됨

print(" === protecet ! ====")
class Quardrangle:
    def __init__(self,width,height,color):
        self._width = width
        self._height = height
        self._color = color
    def get_area(self):
        return self._width * self._height
    def _set_area(self,width,height):
        self._width = width
        self._height = height

square = Quardrangle(5,5,'black')
print(square.get_area())
print(square._width)
square._width = 10
print(square.get_area())
square._set_area(3,3)
print(square.get_area())

print(" === Private ! ====")
# Private
# attribute, method 앞에 __ (double undersocre) 를 붙이면 해당 이름으로 접근 x
# __ 를 붙이면 해당 이름이 _classname__ 해당 속성 또는 메소드 이름으로 변경되기 떄문임
# private 변수 및 함수는 외부에서 접근하도록 설계하면 안됨

class Quardrangle:
    def __init__(self,width,height,color):
        self.__width = width
        self.__height = height
        self.__color = color
    def get_area(self):
        return self.__width * self.__height
    def __set_area(self,width,height):
        self.__width = width
        self.__height =height

square = Quardrangle(5,5,'black')
print(square.get_area())
#square.__width = 10
#square.__set_area(3,3)

# Basic Problem
# Make Circle class
class Circle:
    def __init__(self,radius,name):
        self.__radius = radius
        self.__name = name
    def get_name(self):
        return self.__name

    def get_area(self):
        return 3.14 * self.__radius ** 2

circle = Circle(3,'dave')
print(circle.get_area(),circle.get_name())

print("============= Bank Class ============")
# Bank Class

class Bank:
    def __init__(self,fun,IO_cash):
        self.__B_cash = 0 # 초기금액
        self.IO_cash = IO_cash

        if fun == 1:
            self.__input_cash()
        elif fun ==2:
            self.__out_cash()
        else:
            self.check()

    def __input_cash(self):
        self.__B_cash += self.IO_cash
        return "Current_Account : " ,self.__B_cash


    def __out_cash(self):
        if (self.__B_cash == 0) or (self.__B_cash <0):
            print("Not Exist Cash")
        else:
            self.__B_cash -= self.IO_cash
            return self.__B_cash

    def check(self):
        return self.__B_cash #  남은 금액만 체크




# Directly Access to Private method
# print(mybank._Bank__check())

mybank = Bank(1,1234)
