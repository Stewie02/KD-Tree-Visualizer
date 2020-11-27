import random
from point import Point


class PointCreator:

    def __init__(self, amount_of_points, width, height):
        self.points = []
        for i in range(amount_of_points):
            x = int(random.random() * width)
            y = int(random.random() * height)
            self.points.append(Point(x, y))

        # self.points.append(Point(615, 40))
        # self.points.append(Point(751, 177))
        # self.points.append(Point(207, 313))
        # self.points.append(Point(479, 449))
        # self.points.append(Point(888, 585))
        # self.points.append(Point(70, 721))
        # self.points.append(Point(343, 858))

    def get_points(self):
        return self.points

    def get_point(self, i):
        return self.points[i]
