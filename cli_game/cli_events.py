import string
from pprint import pprint


class InvalidPlayError(Exception):
    # Handle invalid plays
    pass


def convert_input_to_board_position(pos):
    col_pos = ord(pos[0].upper()) - 65  # Converts player input char A - E into int
    row_pos = int(pos[1])
    return (col_pos, row_pos)


def draw_board(board):
    # Draws the game as a 5x5 card matrix
    pprint(board)


def validate_position(board, position):
    col_pos, row_pos = position

    if not ((0 <= col_pos <= 4) and (0 <= row_pos <= 4)):
        raise InvalidPlayError('Out of bounds - play must match format [A,B,C,D,E][0,1,2,3,4]')

    if board[col_pos][row_pos] != 0:
        raise InvalidPlayError('Position is not open')

    if col_pos == 2 and row_pos == 2:
        raise InvalidPlayError('Card cannot be place in the center')


def place_card(board, card, placement):
    col_pos, row_pos = placement
    board[col_pos][row_pos] = card


def play_card(board, player, card):
    play_success = False
    while not play_success:
        draw_board(board)
        print(f'{player}, your card is: {card}')
        try:
            position = convert_input_to_board_position(input('Enter card placement (Ex: A0,B4) >'))
        except ValueError:
            print('Entered values must match format [A,B,C,D,E][0,1,2,3,4]')
        except IndexError:
            print('Input should be two values: [A,B,C,D,E][0,1,2,3,4]')
        else:
            try:
                validate_position(board, position)
            except InvalidPlayError as err:
                print(err)
            else:
                place_card(board, card, position)
                play_success = True