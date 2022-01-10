from aoc_1 import read_data


def main():
    data = read_data(2)
    cmds = []
    for line in data:
        cmd, num = line.split(' ')
        cmds.append((cmd, int(num)))
        
    horiz = 0
    depth = 0
    for c in cmds:
        direction, distance = c
        if direction == 'forward':
            horiz += distance
        elif direction == 'down':
            depth += distance
        elif direction == 'up':
            depth -= distance

    print('horizontal: ', horiz)
    print('depth: ', depth)
    total = horiz * depth
    print('total: ', total)


if __name__ == '__main__':
    main()
