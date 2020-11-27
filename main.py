from kdTree import KdTree
from pointCreator import create_points
from graph import Graph
from lineCreator import get_lines


width = 1200
height = 800
amount_of_points = 10


def main():

    points = create_points(amount_of_points, width, height)
    kd_tree = KdTree(points, False)
    graph = Graph(width, height)

    for point in points:
        graph.show_point(point)

    graph.show_lines(get_lines(kd_tree, width, height))
    graph.run_graph()


if __name__ == "__main__":
    main()
