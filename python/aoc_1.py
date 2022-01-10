def read_data(day):
    with open(f'day{day}_input', 'r') as f:
        return f.read().split('\n')[:-1]


def main():
    data = read_data(1)
    prev = None
    ct = 0

    for d in data:
        if prev and int(d) > prev:
            ct += 1
        
        prev = int(d)

    print(ct)


if __name__ == '__main__':
    main()
