from aoc_1 import read_data


data = read_data(2)
data = [int(k) for k in data]
prev = data[0] + data[1] + data[2]
ct = 0

for k in range(1, len(data) - 2):
    s = data[k] + data[k + 1] + data[k + 2]
    if s > prev:
        ct += 1

    prev = s

print(ct)