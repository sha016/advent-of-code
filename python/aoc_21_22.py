import sys
from aoc_1 import read_data


def check_flashers(grid, flashing, reset):
    flashed = False
    for i in range(0, 10):
        for k in range(0, 10):
            if grid[i][k] > 9 and (i, k) not in reset:
                flashing.append((i, k))
                flashed = True
    return flashed

    
def charge_neighbors(grid, r, c):
    for i in range(r - 1, r + 2):
        for k in range(c -1, c + 2):
            if i == r and k == c:
                continue
            if i < 0 or i > 9 or k < 0 or k > 9:
                continue
            grid[i][k] += 1
            

data = read_data(11)
grid = []
for line in data:
    line = list(line)
    line = [int(k) for k in line]
    grid.append(line)

tot_flashes = 0
part = 2
if part == 1:
    steps = 100
else:
    steps = 1
    
while steps:
    if part == 1:
        steps -= 1
    else:
        steps += 1
    # increment
    for i in range(0, 10):
        for k in range(0, 10):
            grid[i][k] += 1
    
    flashing = []
    reset = []
    # check for flashes
    while check_flashers(grid, flashing, reset):
        while flashing:
            r, c = flashing.pop()
            reset.append((r, c))
            charge_neighbors(grid, r, c)

    # reset those that flashed
    while reset:
        octo = reset.pop()
        tot_flashes += 1
        r, c = octo
        grid[r][c] = 0

    # part 2
    if part == 2:
        synchronized = True
        for row in grid:
            check = all([k == 0 for k in row])
            if not check:
                synchronized = False
        
        if synchronized:
            print('synchronized on step ', steps - 1)
            sys.exit()

print(tot_flashes)
