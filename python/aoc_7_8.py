import sys
import copy

from aoc_1 import read_data


def score_board(board, num):
    score = 0
    for row in board:
        for val in row:
            if val != 'x':
                score += val
    
    return score * num


def handle_winning_board(board, num, let_squid_win, winner_boards, winner_list, idx, win):
    """ Convenient function for handling two different conditions of part 1 & part 2. Not ideal in form. """
    if win and not let_squid_win:
        print(score_board(board, num))
        sys.exit()
    elif win and let_squid_win:
        winner_boards.append((copy.deepcopy(board), num))
        winner_list.append(idx)


def main():
    data = read_data(4)
    # part 2, set "let_squid_win" to false for part 1
    let_squid_win = True
    nums = data[0].split(',')
    nums = [int(k) for k in nums]
    all_boards = data[1:]

    all_boards = [k for k in all_boards if k != '']
    boards = []
    line_ct = 0
    board = []

    for row in all_boards:
        row = row.split(' ')
        row = [int(k) for k in row if k != '']
        board.append(row)

        line_ct += 1
        if line_ct % 5 == 0:
            boards.append(board)
            board = []

    winner_boards = []
    winner_list = []
    for num in nums:
        for idx, board in enumerate(boards):
            # skip boards that have already won (let squid win)
            if idx in winner_list:
                continue

            # update board
            for r, row in enumerate(board):
                for c, val in enumerate(row):
                    if val == num:
                        board[r][c] = 'x'

            # check if board has met win condition
            win = False
            # rows
            for row in board:
                win = all([k == 'x' for k in row])
                handle_winning_board(board, num, let_squid_win, winner_boards, winner_list, idx, win)

            # cols
            for col in range(0, 5):
                column = [board[k][col] for k in range(0, 5)]
                win = all([k == 'x' for k in column])
                if win:
                    handle_winning_board(board, num, let_squid_win, winner_boards, winner_list, idx, win)
                    break
            
    if let_squid_win:
        loser, num = winner_boards.pop()
        print(score_board(loser, num))


if __name__ == '__main__':
    main()
