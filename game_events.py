import os
import pygame
import game_setup as setup

def check_valid_play(cardarea, card):
    if card[1] == False:
        print('Move is valid')
        return True
    else:
        print('Invalid move, cannot play here')  # TODO - special alert for center card
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