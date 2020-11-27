from pointCreator import PointCreator
from graph import Graph
from kdTreeBuilder import KdTreeBuilder


width = 1200
height = 800
amount_of_points = 10


def main():

    point_creator = PointCreator(amount_of_points, width, height)
    builder = KdTreeBuilder(point_creator.get_points(), width, height)
    graph = Graph(width, height)

    for point in point_creator.get_points():
        graph.show_point(point)

    graph.show_lines(builder.get_line_coordinates())
    graph.run_graph()


if __name__ == "__main__":
    main()
