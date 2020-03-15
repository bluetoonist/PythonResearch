# Class Inheritance

"""
 추상화 ( abstraction )
  여러 클래스에 중복되는 속성, 메서드를 하나의 기본 클래스로 작성하는 작업

 상속 ( Inheritance )
  기본 클래스의 공통 기능을 물려 받고, 다른 부분만 추가 또는 변경하는 것
    이 떄 기본 클래스는 부모 클래스, Parent, Super ,Base class 라고 부름
  기본 클래스 기능을 물려받는 클래스는 자식 클래스 ,Child ,Sub,Derived class 라고 부름


-> 코드 재사용이 가능, 공통 기능의 경우 기본 클래스 코드만 수정하면 된다는 장점
    부모 클래스가 둘 이상인 경우는 다중 상속이라고 부름

"""

class Figure:
    def __init__(self,name ,color):
        self.name = name
        self.color = color

class Quardrangle(Figure):

    def set_area(self,width,height):
        self.__width = width
        self.__height = height

    def get_info(self):
        print(self.name,self.color,self.__width*self.__height)

sqaure = Quardrangle('dave','blue')

print(sqaure.name)
sqaure.set_area(5,5)
print(sqaure.get_info())

# 상속 관계 클래스 확인하기
# 내장 함수 issubclass( Quardrangle, Figure)
print(issubclass(Quardrangle,Figure))