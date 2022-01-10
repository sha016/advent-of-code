from aoc_1 import read_data


def main():
    data = read_data(2)
    cmds = []
    for line in data:
        cmd, num = line.split(' ')
        cmds.append((cmd, int(num)))

    horizontal = 0
    aim = 0
    depth = 0
    for cmd in cmds:
        direction, distance = cmd
        if direction == 'forward':
            horizontal += distance
            if aim != 0:
                depth += distance * aim
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance

    print('horizontal: ', horizontal)
    print('depth: ', depth)
    total = horizontal * depth
    print('total: ', total)

if __name__ == '__main__':
    main()
