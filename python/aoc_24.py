from collections import defaultdict

from aoc_1 import read_data
from aoc_23 import Node, init_nodes


ALL_PATHS = []

def valid_path(path, next):
    small_caves = defaultdict(int)
    for c in path:
        if c == c.lower():
            small_caves[c] += 1
    small_caves[next] += 1
    ct = 0
    for _, v in small_caves.items():
        if v > 1:
            ct += 1
    if ct > 1:
        return False

    return True

def recurse_nodes(curr, path):
    """ Explore all paths beginning at "curr"
    append them to paths once 'end' is reached. 
    """
    path = path + [curr.name]
    if curr.name == 'end':
        ALL_PATHS.append(path)        
        return path
    
    for next in curr.connections:
        # tweak logic to follow new rules
        if next.name.lower() == next.name and path.count(next.name) > 1 or not valid_path(path, next.name):
            continue
        if next.name == 'start':
            continue

        recurse_nodes(next, path)

data = read_data(12)
nodes = init_nodes(data)
start_node = nodes.get('start')
recurse_nodes(start_node, [])
print(len(ALL_PATHS))
