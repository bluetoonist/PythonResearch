class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        if bases != (object,):
            if class_dict['sides'] < 3: # sides가 3 밑이면 ValueError를 일으킴
                raise ValueError("Polygons need 3+ sides")
        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3

print("Before Class")


class Line(Polygon):
    print("Before sides")
    sides = 1 # sides를 1로 정의함
    print("After sides")


print("After class")
