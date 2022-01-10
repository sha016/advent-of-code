from aoc_1 import read_data


def main():
    data = read_data(3)
    num_cols = len(data[0])
    num_rows = len(data)
    gamma = ''
    epsilon = ''
    for col in range(0, num_cols):
        zeros = 0
        ones = 0
        for row in data:
            if row[col] == "0":
                zeros += 1
            else:
                ones += 1
            if zeros > num_rows / 2:
                gamma = gamma + "0"
                break
            if ones > num_rows / 2:
                gamma = gamma + "1"
                break

    epsilon = ''.join(["1" if k == "0" else "0" for k in gamma])
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    res = gamma * epsilon
    print(res)


if __name__ == '__main__':
    main()
