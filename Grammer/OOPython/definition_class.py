
"""
Hot to Definition

    keyword
    class class_name:
        pass


"""

class Quadrangle:
    width = 0
    height = 0
    color = 'block'
    
    def get_area(self):
        return self.width*self.height

    def set_area(self,data1,data2):
        self.width = data1
        self.height = data2


class Dave:
    data = 0
    name = "dave"


class SingleWord:
    pass


square1 = Quadrangle()
square2 = Quadrangle()

square1.set_area(10,5)
square2.set_area(7,7)

square1.color = 'red'
square2.color ='blue'

print(square1.get_area())
print(square2.get_area())