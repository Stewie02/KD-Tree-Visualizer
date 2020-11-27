

class KdTree:

    def __init__(self, points, depth):
        self.left = None
        self.right = None
        self.median = None
        self.smaller_than_points = []
        self.bigger_or_equal_points = []
        self.depth = depth
        self.set_points(self.sort_togo_points(points))
        self.left = self.create_child(self.left, self.smaller_than_points)
        self.right = self.create_child(self.right, self.bigger_or_equal_points)

    def create_child(self, side, points):
        if len(points) < 2:
            if not len(points) == 0:
                side = points[0]
        else:
            side = KdTree(points, self.depth + 1)
        return side

    def set_points(self, points):
        self.median = points[int(len(points) / 2)]
        bigger_or_equal = False
        for point in points:
            if point == self.median:
                bigger_or_equal = True
            if not bigger_or_equal:
                self.smaller_than_points.append(point)
            else:
                self.bigger_or_equal_points.append(point)

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def sort_togo_points(self, points):
        for num in range(len(points) - 1, 0, -1):
            for i in range(num):
                if self.get_right_coordinate(points[i]) > self.get_right_coordinate(points[i + 1]):
                    temp = points[i]
                    points[i] = points[i + 1]
                    points[i + 1] = temp
        return points

    def axis_is_vertical(self):
        return self.depth % 2 == 0

    def get_right_coordinate(self, point):
        return point.get_x() if self.axis_is_vertical() else point.get_y()

    def get_median(self):
        return self.median
