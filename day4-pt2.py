import sys
from typing import Optional
from utils import read_input


def get_numbers(string: str):
    return [int(char) for char in string.split(' ') if char != '']


def generate_player_boards(bingo_numbers):
    players_boards = []
    for player_start_idx in range(0, len(bingo_numbers), 5):
        players_board = bingo_numbers[player_start_idx: player_start_idx + 5]
        players_board = [get_numbers(row) for row in players_board]
        players_boards.append([*players_board])
    return players_boards


def check_win(player_board: list[list[Optional[int]]]):
    for row in player_board:
        if all(cell == None for cell in row):
            return True
    for col in zip(*player_board):
        if all(cell == None for cell in col):
            return True


def update_board(number, player_board: list[list[int]]):
    for i, row in enumerate(player_board):
        for j, cell in enumerate(row):
            if number == cell:
                player_board[i][j] = None

    if check_win(player_board):
        return player_board
    return False


def calculate_score(winning_board, winning_number):
    total = sum(sum(cell for cell in row if cell != None)
                for row in winning_board) * winning_number
    print(total)


def start_game(number_list, player_boards):
    total_boards_won = set()
    for number in number_list:
        for i, player_board in enumerate(player_boards):
            if i in total_boards_won:
                continue
            else:
                winning_players_board = update_board(number, player_board)
                if winning_players_board:
                    if len(total_boards_won) == len(player_boards) - 1:
                        return calculate_score(winning_players_board, number)
                    else:
                        total_boards_won.add(i)


def main():
    values = read_input('input-day-4.txt')
    number_list, bingo_numbers = values[0], values[1:]
    player_boards = generate_player_boards(bingo_numbers)
    number_list = [int(number) for number in number_list.split(',')]
    start_game(number_list, player_boards)


if __name__ == '__main__':
    sys.exit(main())
