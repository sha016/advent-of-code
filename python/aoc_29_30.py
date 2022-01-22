from copy import deepcopy
from queue import PriorityQueue

from aoc_1 import read_data


class Node:

    def __init__(self, x, y, val, end_x, end_y):
        self.x = x
        self.y = y
        self.end_x = end_x
        self.end_y = end_y
        self.val = val
        self.connections = []
        self.visited = False
        self.parent = None
        self.add_connections()

    def add_connections(self):
        for i in range(self.x - 1, self.x + 2):
            for k in range(self.y - 1, self.y + 2):
                if i < 0 or i > self.end_x or k < 0 or k > self.end_y:
                    continue
                # exclude diagonals
                elif abs(self.x - i + self.y - k) == 1:
                    self.connections.append((i, k))

    def distance_to_end(self):
        return (self.end_x - self.x) + (self.end_y - self.y)

    def distance_from_start(self):
        return self.x + self.y

    def get_path_cost(self):
        tot = 0
        tot += self.val
        parent = self.parent
        while parent:
            tot += parent.val
            parent = parent.parent
        return tot

    def __lt__(self, other):
        if self.distance_to_end() < other:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.distance_to_end() > other:
            return True
        else:
            return False

    def __repr__(self):
        return f'({self.x}, {self.y})'


def main():
    # read and parse data
    data = read_data(15)
    grid = []
    for line in data:
        tmp = list(line)
        grid.append([int(k) for k in tmp])

    part = 2
    if part == 2:
        # create the progression of values for the first "column" of grids.
        new_grid = [[] for _ in range(len(grid) * 5)]
        offset = 0
        row_offset = 0
        while offset < 5:
            for n in range(offset, offset + 5):
                tmp = deepcopy(grid)
                for i in range(0, len(tmp)):
                    for k in range(0, len(tmp)):
                        incr = tmp[i][k] + n
                        if incr > 9:
                            incr -= 9
                        new_grid[(row_offset // len(grid))].append(incr)
                        row_offset += 1

                offset += 1

        # increment columns by 1 going to the right
        cols = 4
        while cols:
            for row in new_grid:
                ext = [v + 1 if v + 1 <= 9 else v + 1 - 9 for v in row[0-len(grid[0]):]]
                row.extend(ext)
            cols -= 1

    # init nodes and nearby coords
    if part == 1:
        end_x = 99
        end_y = 99
    else:
        end_x = 499
        end_y = 499
        grid = new_grid

    nodes = []
    node_dict = {}
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            node = Node(x, y, val, end_x, end_y)
            nodes.append(node)
            node_dict[(x, y)] = node

    best_path = {}
    for node in node_dict.values():
        best_path[node] = float('inf')
        tmp = []
        for conn in node.connections:
            n = node_dict.get((conn[0], conn[1]))
            tmp.append(n)
        node.connections = tmp
    
    tot_risk = 0
    best_guess = {}
    Q = PriorityQueue()
    root = nodes[0]
    Q.put((0, root))
    end = None
    while Q.not_empty:
        """ While there are nodes in the queue, 
        pop off highest priority nodes and push neighbors. 
        """
        _, curr = Q.get()
        tot_risk += curr.val
        curr.visited = True
        if curr.x == end_x and curr.y == end_y:
            end = curr
            break

        for k in curr.connections:
            if k is None:
                continue
            if k.visited:
                continue

            move_cost = curr.get_path_cost() + k.val
            if move_cost < best_path.get(k):
                best_path[k] = move_cost
                best_guess[k] = move_cost + k.distance_to_end()
                Q.put((move_cost + k.distance_to_end(), k))
                k.parent = curr

    path = end.val
    ct = 0
    prev = end.parent
    while prev.parent:
        path += prev.val
        prev = prev.parent
        ct += 1
    
    print(path, 'risk in', ct, 'steps')


if __name__ == '__main__':
    main()
