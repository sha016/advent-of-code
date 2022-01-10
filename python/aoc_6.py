from aoc_1 import read_data


def get_rating(data, col, mode):
    if len(data) == 1:
        return int(data[0], 2)
    
    keep = []
    zero = one = 0
    targ = ''
    for r in data:
        if r[col] == "1":
            one += 1
        else:
            zero += 1

    if one > zero:
        targ = "1"
    elif zero > one:
        targ = "0"
    elif zero == one:
        targ = "1"

    for r in data:
        if r[col] == targ and mode == 'oxygen':
            keep.append(r)
        if r[col] != targ and mode == 'c02':
            keep.append(r)

    return get_rating(keep, col + 1, mode)

def main():
    data = read_data(3)
    oxygen_generator_rating = get_rating(data, 0, 'oxygen')
    co2_scrubber_rating = get_rating(data, 0, 'c02')
    res = oxygen_generator_rating * co2_scrubber_rating
    print(res)


if __name__ == '__main__':
    main()
