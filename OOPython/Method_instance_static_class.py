"""

instance method : 해당 객체 안에서 호출(self.메서드명)
해당 메서드를 호출한 객체에만 영향을 미침
객체 속성에 접근 가능

static method : 객체와 독립적인지만,로직상 클래스내에 포함되는 메서드

self 파라미터를 가지고 있지 않음
객체 속성에 접근 불가
정적 메서드는 메서드 앞에 @staticmethod라는 Decorator를 넣음
클래스명.정적메서드명 또는 객체명.정적메서드명 둘 다 호출 가능

"""

class Figure:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def clac_area(self):
        return self.width*self.height

    @staticmethod
    def is_square(rect_width,rect_height):
        if rect_width == rect_height:
            print("정사각형이 될 수 있는 너비/높이임")
        else:
            print("정사각형이 될 수 없는 너비/높이임")

figure1 = Figure(2,3)

# Instance Method
figure1.is_square(5,5) # 객체명.정적메서드명으로 호출 가능

# static Method
Figure.is_square(4,5)  # 클래스명.정적메서드명으로 호출 가능

print("==============================")

# Class Method 클래스 메서드
# 해당 클래스로 만들어진 객체에서 호출되지 않고 직접 클래스 자체에서 호출
"""
 self 파라미터 대신 ,cls 파라미터를 가짐
 클래스 변수 접근 가능하며 cls.클래스 변수명으로 액세스 가능 단, 객체 속성/메서드는 접근 불가
 @classmethod 라는 Decorator를 넣음
 클래스명.클래스메서드명 또는 객체명,.클래스메서드명 둘 다 호출 가능

"""
class Figure1:
    count = 0
    def __init__(self,width,height):
        self.width = width
        self.height = height
        Figure1.count +=1

    def clac_area(self):
        return self.width*self.height

    @classmethod
    def print_count(cls):
        return cls.count

figure1 = Figure1(2,3)
figure2 = Figure1(4,5)
print(Figure1.count) # 클래스 변수 호출
print(Figure1.print_count()) # 클래스 메서드 호출
print(figure1.print_count()) # 인스턴스 변수 호출

print("="*40)

class A(object):
    count = 0 # static member ( class variable)
    def __init__(self,cnt):
        A.count +=1
        self.cnt = cnt # member variable , attribute

    def print_cnt(self): # member funtion, method
        print(self.cnt)

    @classmethod # class method , static function
    def print_count(cls):
        print(cls.count)

a1 = A(1)
a2 = A(2)
a3 = A(44)

a1.print_cnt()
a2.print_cnt()
a3.print_cnt()

A.print_count()