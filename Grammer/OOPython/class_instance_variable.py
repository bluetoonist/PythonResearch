"""
클래스 변수
클래스 정의에서 메서드 밖에 존재하는 변수

 해당 클래스를 사용하는 모두에게 공용으로 사용되는 변수

 클래스 변수는 클래스 내외부에서 클래스명.변수명으로 액세서 가능


인스턴스 변수
클래스 정의에서 메서드 안에서 사용되면 self.변수명 처럼 사용되는 변수

 각 객체별로 서로 다른 값을 가짐

 클래스 내부에서는 self.인스턴스변수 명을 사용하여 액세스, 클래스 밖에서는
 객체명.인스턴스변수명으로 액세스

"""
class Figure:
    count = 0 # 클래스 변수
    def __init__(self,width,height):
        # self 인스턴스 변수
        self.width = width
        self.height = height
        Figure.count +=1
    def __del__(self):
        Figure.count -=1

    def calc_area(self): # Method
        return self.width*self.height

print(Figure.count)
figure1 = Figure(2,3)
print(Figure.count)
figure2 = Figure(2,3)
print(Figure.count)
