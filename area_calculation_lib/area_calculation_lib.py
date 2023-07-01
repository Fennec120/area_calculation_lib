#base class
class area_calculator:
    def __init__(self):
        pass

    #providing triangle sides' lengths
    def triangle_set_params(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    # providing round radius' length
    def round_set_params(self, rad):
        self.rad = rad

    #triangle area calculation w\ additional checking for right angle
    def triangle_area(self):
        import math

        pp = (self.side_1 + self.side_2 + self.side_3) / 2

        if self.side_1 ** 2 == self.side_2 ** 2 + self.side_3 ** 2 or \
                self.side_3 ** 2 == self.side_1 ** 2 + self.side_2 ** 2 or \
                self.side_2 ** 2 == self.side_1 ** 2 + self.side_3 ** 2:
            print(
                f'{math.sqrt(pp * (pp - self.side_1) * (pp - self.side_2) * (pp - self.side_3))}, Прямоугольный треугольник')
            return math.sqrt(pp * (pp - self.side_1) * (pp - self.side_2) * (pp - self.side_3))

        return math.sqrt(pp * (pp - self.side_1) * (pp - self.side_2) * (pp - self.side_3))

    #round area calculation
    def round_area(self):
        print(self.rad ** 2 * 3.14)
        return self.rad ** 2 * 3.14

