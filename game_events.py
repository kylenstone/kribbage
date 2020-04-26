import os
import pygame



def place_card(card):
    return

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