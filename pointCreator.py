import random
from point import Point


def create_points(amount_of_points, width, height):
    points = []
    for i in range(amount_of_points):
        x = int(random.random() * width)
        y = int(random.random() * height)
        points.append(Point(x, y))
    return points
