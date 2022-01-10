from aoc_1 import read_data


class Basin:

    def __init__(self, grid, bottom):
        self.grid = grid
        self.bottom = bottom
        self.basins = []
        self.scanned = []
        self.y, self.x = self.bottom

    def scan(self, y, x):
        """ Check adjacent locations for undiscovered basins."""
        basins = []
        if self.y - 1 >= 0 and self.grid[self.y - 1][self.x] != 9 and (y - 1, x) not in self.basins:
            basins.append((y -1, x))
        if self.y + 1 < 100 and self.grid[self.y + 1][self.x] != 9 and (y + 1, x) not in self.basins:
            basins.append((y + 1, x))
        if self.x - 1 >= 0 and self.grid[self.y][self.x - 1] != 9 and (y, x - 1) not in self.basins:
            basins.append((y, x - 1))
        if self.x + 1 < 100 and self.grid[self.y][self.x + 1] != 9 and (y, x + 1) not in self.basins:
            basins.append((y, x + 1))
        
        return basins

    def run(self):
        """ Do a sweep of adjacent valid basins and then sweep from those basins. """
        while True:
            if (self.y, self.x) not in self.basins:
                self.basins.append((self.y, self.x))
            self.scanned.extend(self.scan(self.y, self.x))
            if not self.scanned:
                break
            new = self.scanned.pop()
            self.y, self.x = new
        
        return self.basins


def main():
    data = read_data(9)
    grid = []
    low_points = []
    for row in data:
        grid.append([int(k) for k in list(row)])

    # part 1
    for r, row in enumerate(grid):
        for c, val in enumerate(row):

            if r > 0 and grid[r - 1][c] <= val:
                continue

            if c > 0 and grid[r][c - 1] <= val:
                continue

            if r + 1 < len(grid) and grid[r + 1][c] <= val:
                continue

            if c + 1 < len(row) and grid[r][c + 1] <= val:
                continue

            low_points.append((r, c))

    risk_sum = 0
    for k in low_points:
        r, c = k
        risk_sum += int(grid[r][c]) + 1

    print('part 1: ', risk_sum)

    # part 2
    sizes = []
    for p in low_points:
        r, c = p
        basin = Basin(grid, p)
        basins = basin.run()
        sizes.append(len(basins))

    top_3 = 1
    sizes.sort()
    for s in sizes[-3:]:
        top_3 *= s

    print('part 2: ', top_3)


if __name__ == '__main__':
    main()
