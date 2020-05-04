# Library imports
import os
import pygame

#Local imports
import game_setup as setup

def check_valid_play(spot):
    if spot.is_open == True:
        print('Move is valid')
        return True
    else:
        print('Invalid move, cannot play here')
        return False

# def play_move(card, loc):
    # TODO - calls check_valid_play?
#     if is_valid_play(loc, used_moves):
#         screen.blit(datadeck.pop(0)[2], moveloc)
#         screen.blit(datadeck[0][2], (datadeck[0][1].x, datadeck[0][1].y))
#         p1turn = False
#     else:
#         print("False")
#     return datadeck

# def render_to_gui(Rect, Surface):
    # if Rect is newly created, simply blit Rect to location
    # if Rect already exists, call Rect.move() then blit new location

def reveal_card_in_board_center(screen, ctrcard):
    return setup.render_card(screen, ctrcard.card, (ctrcard.rect.x, ctrcard.rect.y))