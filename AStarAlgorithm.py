import numpy as np
import math


class Node:

    def __init__(self, pos, parent = None):
        self.parent = parent
        self.pos = pos

        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.pos == other.pos


def path_step_wise(maze, end, open_list, closed_list):
    done = False
    node_open_list, node_closed_list = search_alg_step_wise(maze, end, open_list, closed_list)

    if tuple(node_closed_list[-1].pos) == tuple(end.pos):
        done = True

    return done, node_closed_list, node_open_list


def search_alg_step_wise(maze, end, open_list, closed_list):
    no_columns, no_rows = np.shape(maze)

    if len(open_list) > 0:

        current_index = 0

        for index in range(len(open_list)):
            if open_list[index].f < open_list[current_index].f:
                current_index = index

        current_node = open_list[current_index]

        open_list.pop(current_index)
        closed_list.append(current_node)
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
            if node not in closed_list:
                temp_g = current_node.g + 1
                if node in open_list:
                    if node.g > temp_g:
                        node.g = temp_g
                else:
                    node.g = temp_g
                    open_list.append(node)

            node.h = math.sqrt((node.pos[0] - end.pos[0]) ** 2 + (node.pos[1] - end.pos[1]) ** 2)
            node.f = node.g + node.h

            if node.parent is None:
                node.parent = current_node

        return open_list, closed_list



