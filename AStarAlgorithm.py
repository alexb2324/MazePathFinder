import numpy as np
import math

open_list = []
closed_list = []



class Node:

    def __init__(self, pos, parent = None):
        self.parent = parent
        self.pos = pos

        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.pos == other.pos


start = Node([0, 0], None)
start.f = start.g = start.h = 0
end = Node([29,29], None)
end.f = end.g = end.h = 0

open_list.append(start)



def path_step_wise(maze):
    done = False

    node_open_list, node_closed_list = search_alg_step_wise(end, maze)

    if tuple(node_closed_list[-1].pos) == tuple(end.pos):
        done = True

    return done, node_closed_list, node_open_list






def search_alg_step_wise(end, maze):
    no_columns, no_rows = np.shape(maze)

    if len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

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

            if len([past_node for past_node in closed_list if past_node == node]) > 0:
                continue

            node.g = current_node.g + 1
            node.h = math.sqrt((node.pos[0] - end.pos[0]) ** 2 + (node.pos[1] - end.pos[1]) ** 2)
            node.f = node.g + node.h

            if len([i for i in open_list if node == i and node.g > i.g]) > 0:
                continue

            open_list.append(node)

        return open_list, closed_list



