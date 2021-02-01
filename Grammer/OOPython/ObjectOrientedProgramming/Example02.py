
class Flight:
    class_attr = [] # 클래스 속성 -> 여러 객체가 공유함
    __private_attr = 5 # 비공개 클래스 속성
    def add_class_attr(self,number):
        Flight.class_attr.append(number)

f = Flight()
g = Flight()

f.add_class_attr(5)

print(Flight.class_attr)
print(f.class_attr)
print(g.class_attr)