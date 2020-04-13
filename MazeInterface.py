import numpy as np
import math


class Node:

    def __init__(self, pos, parent=None):
        self.parent = parent
        self.pos = pos

        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.pos == other.pos


def path(maze):
    start = Node([0, 0], None)
    start.f = start.g = start.h = 0
    end = Node([29, 29], None)
    end.f = end.g = end.h = 0

    path_nodes = search_alg(start, end, maze)
    path_list = [tuple(node.pos) for node in path_nodes]

    return path_list


def search_alg(start, end, maze):
    open_list = []
    closed_list = []
    no_columns, no_rows = np.shape(maze)

    open_list.append(start)
    count = 0
    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end:
            return closed_list

        i = current_node.pos[0]
        j = current_node.pos[1]
        current_movement_list = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1], [i - 1, j - 1], [i + 1, j + 1],
                                 [i - 1, j + 1], [i + 1, j - 1]]

        node_list = []
        for pos in current_movement_list:

            if ((pos[0] > (no_rows - 1)) or
                    (pos[0] < 0) or
                    (pos[1] > (no_columns - 1)) or
                    (pos[1] < 0)):
                continue

            if maze[pos[0]][pos[1]] != 0:
                continue

            new_node = Node(pos, current_node)
            node_list.append(new_node)

        for node in node_list:

            if node in closed_list:
                val_index = closed_list.index(node)
                if closed_list[val_index].f < node.f:
                    open_list.append(closed_list[val_index])
                    continue

            node.g = current_node.g + 1
            node.h = math.sqrt((node.pos[0] - end.pos[0]) ** 2 + (node.pos[1] - end.pos[1]) ** 2)
            node.f = node.g + node.h

            if node in open_list:
                val_index = open_list.index(node)
                print("hello")
                if open_list[val_index].f < node.f:
                    continue

            open_list.append(node)
            print(node.pos)
            count += 1
            print(count)






