import os
import pygame
import game_setup as setup


def play_card(player, deck, round):
    # Called each time p1 or p2 plays a card.
    player = player
    card = deck[round]
    play_success = False
    while not play_success:
        try:
            print(f'{player} Your card is: {card}')
            draw_board()
            pos = input('Enter card placement (Ex: A0,B4) >')
            col_pos, row_pos = input_to_str(pos)
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

def is_play_valid(col_pos, row_pos):
    # Each play must be on an open spot that is not the board center (pos[B2])
    col_pos = col_pos
    row_pos = row_pos
    assert board[col_pos][row_pos] == 0
    assert col_pos != 2 or row_pos != 2

# def handle_click:
    # Moves card to the position on board
    # Render the card
    # which_spot_pos(mouse_position) -- gets position from mouse @click
    # Checks is_valid_move?
    # Checks to see if spot is real

def is_play_valid(col_pos, row_pos):
    # Each play must be on an open spot that is not the board center (pos[B2])
    col_pos = col_pos
    row_pos = row_pos
    assert board[col_pos][row_pos] == 0
    assert col_pos != 2 or row_pos != 2