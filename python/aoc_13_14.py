from aoc_1 import read_data


def main():
    data = read_data(7)
    data = [int(k) for k in data[0].split(',')]
    best = 999999999
    best_pos = None
    constant_rate = False
    for pos in range(0, len(data)):
        fuel = 0
        for crab in data:
            base_cost = abs(crab - pos)
            if constant_rate:
                cost = base_cost
            else:
                cost = sum([k for k in range(1, base_cost + 1)])
            fuel += cost
        if fuel < best:
            best = fuel
            best_pos = pos
        
    print(best, best_pos)


if __name__ == '__main__':
    main()
