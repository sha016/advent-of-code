from aoc_1 import read_data


def main():
    data = read_data(8)
    signals = []
    outputs = []

    # part 1
    for line in data:
        sig, out = line.split(' | ')
        signals.append(sig)
        outputs.append(out)

    uniques = 0
    for row in outputs:
        words = row.split(' ')
        for word in words:
            length = len(word)
            if length == 2 or length == 4 or length == 3 or length == 7:
                uniques += 1
        
    print('part 1: ', uniques)

    # part 2
    tot = 0
    for row, output in zip(signals, outputs):
        words = row.split(' ')
        zero =  ''
        one =   ''
        two =   ''
        three = ''
        four =  ''
        five =  ''
        six =   ''
        seven = ''
        eight = ''
        nine = ''
        for word in words:
            # given
            if len(word) == 2:
                one = word
            elif len(word) == 4:
                four = word
            elif len(word) == 3:
                seven = word
            elif len(word) == 7:
                eight = word
        
        for word in words:
            # deduced
            if len(word) == 5 and len(set(word).intersection(one)) == 2:
                three = word
            elif len(word) == 5 and len(set(word).difference(set(four))) == 3 and len(set(word).difference(set(one))) == 4:
                two = word
            elif len(word) == 5 and len(set(word).difference(set(four))) == 2 and len(set(word).difference(set(one))) == 4:
                five = word

        for word in words:
            # further deduced
            if set(word) == set(five).union(set(one)):
                nine = word
            elif len(word) == 6 and len(set(word).difference(one)) == 5:
                six = word
            elif len(word) == 6 and len(set(word).union(set(five))) == 7:
                zero = word

        mapping = {
            zero: 0,
            one: 1,
            two: 2,
            three: 3,
            four: 4,
            five: 5,
            six: 6,
            seven: 7,
            eight: 8,
            nine: 9,
        }

        vals = output.split(' ')
        val = ''
        for i in vals:
            for k, v in mapping.items():
                if set(k) == set(i):
                    val = val + str(v)
            
            
        tot += int(val)

    print('part 2: ', tot)


if __name__ == '__main__':
    main()
