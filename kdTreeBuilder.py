import copy

from kdTree import KdTree
from line import Line
from point import Point


def create_boundaries(boundary, is_vertical, median):
    left = copy.copy(boundary)
    right = copy.copy(boundary)
    if is_vertical:
        left.max_x = median.get_x()
        right.min_x = median.get_x()
    else:
        left.max_y = median.get_y()
        right.min_y = median.get_y()
    return left, right


def get_line_coordinates_aux(line_list, c, boundary):
    if c is not None and not type(c) == Point:
        median = c.get_median()
        is_vertical = c.axis_is_vertical()

        begin_x = median.get_x() if is_vertical else boundary.min_x
        end_x = median.get_x() if is_vertical else boundary.max_x
        begin_y = boundary.min_y if is_vertical else median.get_y()
        end_y = boundary.max_y if is_vertical else median.get_y()
        line_list.append(
            Line(
                begin_x, begin_y,
                end_x, end_y
            )
        )
        left_boundary, right_boundary = create_boundaries(boundary, is_vertical, median)
        get_line_coordinates_aux(line_list, c.get_left(), left_boundary)
        get_line_coordinates_aux(line_list, c.get_right(), right_boundary)


class KdTreeBuilder:

    def __init__(self, points, width, height):
        self.head = KdTree(points, False)
        self.width = width
        self.height = height

    def get_head(self):
        return self.head

    def get_line_coordinates(self):
        line_list = []
        get_line_coordinates_aux(line_list, self.head, Boundary(0, self.width, 0, self.height))
        return line_list


class Boundary:

    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
