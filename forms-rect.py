
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y


class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side

class rect(Square):
    def __init__(self, side1=1, side2=1, x=0, y=0):
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2

    def bloop(self):
        self.side2 = self.side1

class Circle(Shape):
    pi = 3.14159
    all_circles = []

    def __init__(self, radius=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius
        self.all_circles.append(self)

    @classmethod
    def total_area(cls):
        area = 0
        for circle in cls.all_circles:
            area += cls.circle_area(circle.radius)
        return area

    @staticmethod
    def circle_area(radius):
        return __class__.pi * radius * radius

    @staticmethod
    def sq_area(side):
        return side * side
