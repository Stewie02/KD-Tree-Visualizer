import copy
from line import Line
from boundary import Boundary
from point import Point


def get_lines(head, width, height):
    line_list = []
    get_line_coordinates_aux(line_list, head, Boundary(0, width, 0, height))
    return line_list


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
