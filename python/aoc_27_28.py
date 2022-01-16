from collections import Counter

from aoc_1 import read_data


def parse_data(data):
    template = data[0]
    insertions = {}
    for line in data[2:]:
        pair, char = line.split(' -> ')
        insertions[pair] = char
    
    return template, insertions


def main():
    data = read_data(14)
    template, insertions = parse_data(data)

    part = 2
    steps = 40 if part == 2 else 10
    c = Counter()
    for k, _ in insertions.items():
        if k in template:
            c[k] += template.count(k)

    symbol_ct = Counter()  
    for symbol in template:
        symbol_ct[symbol] += 1
    
    while steps:
        tmp = Counter(c)
        for pair, ct in c.items():
            if ct == 0:
                continue
            ins = insertions.get(pair)
            symbol_ct[ins] += ct
            new1 = pair[0] + ins
            new2 = ins + pair[1]
            # destroy pairs
            tmp[pair] -= ct
            # increment two newly created pairs
            tmp[new1] += ct
            tmp[new2] += ct

        c = tmp
        steps -= 1

    print(symbol_ct.most_common(1)[0][1] - symbol_ct.most_common()[-1][1])


if __name__ == '__main__':
    main()
