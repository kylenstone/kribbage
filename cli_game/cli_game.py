import pydealer as dealer
import setup
from pprint import pprint
# pydealer is used to generate game objects.  Docs: https://pydealer.readthedocs.io/en/latest/usage.html#install-uninstall-with-pip

import string

deck = setup.create_deck()
board = setup.create_board()

round_over = False
plays_on_board = 0

# Deal out cards, including card at center of board.
p1deck = deck.deal(12)
p2deck = deck.deal(12)
ctrcard = deck.deal(1)

def convert_input_to_board_position(pos):
    col_pos = ord(pos[0].upper()) - 65 # Converts player input char A - E into int
    row_pos = int(pos[1])
    return col_pos, row_pos

def draw_board():
    # Draws the game as a 5x5 card matrix
    pprint(board)

def play_card(player, card):
    # Called each time p1 or p2 plays a card.
    play_success = False
    while not play_success:
        try:
            draw_board()
            print(f'{player}, your card is: {card}')
            col_pos, row_pos = convert_input_to_board_position(input('Enter card placement (Ex: A0,B4) >'))
            is_play_valid(col_pos, row_pos)
        except IndexError as error:
            print('Out of bounds. Play must be in format [A,B,C,D,E][0,1,2,3,4]')
        except AssertionError as error:
            print(error)
            print('Play was not in an available space. Try again')
        except ValueError as Error:
            print('Invalid input. Play must be in format \'A0\', etc.')
        else:
            board[col_pos][row_pos] = card
            play_success = True
        return card

def is_play_valid(col_pos, row_pos):
    # Each play must be on an open spot that is not the board center (pos[B2])
    assert board[col_pos][row_pos] == 0
    assert col_pos != 2 or row_pos != 2

while not round_over:
    # P1
    card = play_card('p1', p1deck.get(0))

    # P2
    card = play_card('p2', p2deck.get(0))

    # End the game when 24 cards are played
    if plays_on_board>=24:
        round_over = True
        print('game over! ')
        print('turn over center card...')
        print('final board:')
        draw_board()
        # Note: counting scores will be hard in CLI version!