from aoc_1 import read_data


def fish_buckets(arr, days):
    while days:
        baby_fish = arr[0]
        babies = baby_fish
        reset_fish = baby_fish
        arr[0] = 0
        for k in range(1, len(arr)):
            while arr[k]:
                arr[k -1] += arr[k]
                arr[k] = 0
        
        if baby_fish:
            arr[8] = babies
            arr[6] += reset_fish
            
        days -= 1

    return arr


def main():
    data = read_data(6)
    fish_list = data[0].split(',')
    fish_list = [int(k) for k in fish_list]
    days = 256
    arr = [0 for _ in range(0, 9)]
    for fish in fish_list:
        arr[fish] += 1

    test = fish_buckets(arr, days)
    print(sum(test))


if __name__ == '__main__':
    main()
