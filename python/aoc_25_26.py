from aoc_1 import read_data


def main():
    part = int(input('Which part of this day would you like computed? '))
    data= read_data(13)
    folds = []
    while 'fold' in data[-1]:
        folds.append(data.pop())

    data.pop()
    max_x = 0
    max_y = 0
    coords = []
    for line in data:
        x, y = line.split(',')
        x, y = int(x), int(y)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        coords.append((x, y))

    grid = [['.'] * (max_x + 1) for _ in range(0, max_y + 1)]
    for coord in coords:
        x, y = coord
        grid[y][x] = '#'
    
    while folds:
        instr = folds.pop().split(' ')[-1]
        axis, pt = instr.split('=')
        pt = int(pt)
        # transpose below fold points
        new_coords = []
        for i, row in enumerate(grid):
            for k, col in enumerate(row):
                if axis == 'y' and i > pt and col == '#':
                    new_coords.append((k, pt - i))
                elif axis == 'x' and k > pt and col == '#':
                    new_coords.append((pt - k, i))

        # apply fold
        if axis == 'y':
            grid = grid[:pt]
        else:
            new_grid = []
            for row in grid:
                new_grid.append(row[:pt])
            grid = new_grid

        for coord in new_coords:
            x, y = coord
            grid[y][x] = '#'

        if part == 1:
            ct = 0
            for row in grid:
                for c in row:
                    if c == '#':
                        ct += 1
            
            for row in grid:
                print(''.join(row))
            print(ct)
            break

    if part == 2:
        for row in grid:
            print(''.join(row))
            

if __name__ == '__main__':
    main()
