from aoc_1 import read_data


def parse_data(data):
    coords = []
    max_x = 0
    max_y = 0
    for row in data:
        start, end = row.split(' -> ')
        sx, sy = start.split(',')
        sx, sy = int(sx), int(sy)
        ex, ey = end.split(',')
        ex, ey = int(ex), int(ey)
        coords.append( (sx, sy, ex, ey) )
        if sx > max_x:
            max_x = sx
        if ex > max_x:
            max_x = ex
        if sy > max_y:
            max_y = sy
        if ey > max_y:
            max_y = ey
    return coords, max_x, max_y


def main():
    data = read_data(5)
    coords, max_x, max_y = parse_data(data)
    grid = [[0] * (max_x + 1) for _ in range(0, max_y + 1)]
    diagonals = True
    for coord in coords:
        sx, sy, ex, ey = coord
        # only map horizontal or vertical lines
        if sx == ex:
            for k in range(sy if sy < ey else ey, (ey if ey > sy else sy) + 1):
                grid[k][sx] += 1
        elif sy == ey:
            for k in range(sx if sx < ex else ex, (ex if ex > sx else sx) + 1):
                grid[sy][k] += 1
        elif diagonals:
            if sx > ex:
                xr = range(ex, sx + 1)
                xr = [k for k in xr]
                xr.reverse()
            else:
                xr = range(sx, ex + 1)
            if sy > ey:
                yr = range(ey, sy + 1)
                yr = [k for k in yr]
                yr.reverse()
            elif ey > sy:
                yr = range(sy, ey + 1)
            
            for x, y in zip(xr, yr):
                grid[y][x] += 1
                
    unsafe_points = 0
    for row in grid:
        for val in row:
            if val > 1:
                unsafe_points += 1
                
    print(unsafe_points)


if __name__ == '__main__':
    main()
