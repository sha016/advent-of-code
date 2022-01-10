from aoc_9_10 import read_data


def main():
    data = read_data(10)

    SCORES = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    CLOSING = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }

    def is_corrupted(line):
        """ Check for corrupt characters. If found, returns a tuple (True, index) 
        where the index is the first corrupt char. 
        Otherwise, return (False, None) 
        """
        opening = []
        idxs = []
        for idx, c in enumerate(line):
            if c not in CLOSING:
                opening.append(c)
            elif opening[-1] == CLOSING.get(c):
                opening.pop()
            else:
                idxs.append(idx)
                # just the first
                break
                
        if idxs:
            return True, idxs
        else:
            return False, None


    # part 1
    syntax_error_scores = []
    corrupt_idxs = []
    for idx, line in enumerate(data):
        corrupt = is_corrupted(line)
        points = []
        if corrupt[0]:
            corrupt_idxs.append(idx)
            for idx in corrupt[1]:
                pts = SCORES.get(line[idx])
                points.append(pts)

        syntax_error_scores.append(sum(points))

    print('part 1: ', sum(syntax_error_scores))

    # part 2
    SCORES2 = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    OPENING = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'
    }

    def complete_line(line):
        """ Returns a list of the closing characters needed to make the line valid. """
        opening = []
        closing = []
        for c in line:
            if c not in CLOSING:
                opening.append(c)
            elif opening[-1] == CLOSING.get(c):
                opening.pop()
            
        while opening:
            c = opening.pop()
            closing.append(OPENING.get(c))

        return closing

    scores = []
    for idx, line in enumerate(data):
        if idx in corrupt_idxs:
            continue

        closing = complete_line(line)
        score = 0
        for c in closing:
            score *= 5
            score += SCORES2.get(c)
        
        scores.append(score)

    scores.sort()
    print('part 2: ', scores[len(scores) // 2])


if __name__ == '__main__':
    main()
