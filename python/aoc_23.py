from aoc_1 import read_data


ALL_PATHS = []

class Node:

    def __init__(self, name):
        self.name = name
        self.connections = []

    def __repr__(self) -> str:
        return self.name
    

def recurse_nodes(curr, path):
    """ Explore all paths beginning at "curr"
    append them to paths once 'end' is reached. 
    """
    path = path + [curr.name]
    if curr.name == 'end':
        ALL_PATHS.append(path)        
        return path
    
    for next in curr.connections:
        if any([k.lower() == k and k == next.name for k in path]):
            continue
        if next.name == 'start':
            continue
        recurse_nodes(next, path)

def init_nodes(data):
    """ init node objects and connections. """
    nodes = {}
    for line in data:
        e1, e2 = line.split('-')

        if e1 not in nodes:
            e1 = Node(e1)
            nodes[e1.name] = e1
        else:
            e1 = nodes.get(e1)
        
        if e2 not in nodes:
            e2 = Node(e2)
            nodes[e2.name] = e2
        else:
            e2 = nodes.get(e2)
        
        if e2 not in e1.connections:
            e1.connections.append(e2)
        if e1 not in e2.connections:
            e2.connections.append(e1)
    
    return nodes

def main():
    data = read_data(12)
    nodes = init_nodes(data)
    start_node = nodes.get('start')
    recurse_nodes(start_node, [])
    print(len(ALL_PATHS))


if __name__ == '__main__':
    main()
