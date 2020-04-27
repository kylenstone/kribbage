import pydealer as dealer
# pydealer is used to generate game objects.  Docs: https://pydealer.readthedocs.io/en/latest/usage.html#install-uninstall-with-pip
import pygame
from pygame.locals import *
import os, sys
import game_events as events
import game_setup as setup

# Initialize screen
pygame.init()
pygame.display.set_caption("Killer Kribbage!")
width = 1100
height = 800
screen = pygame.display.set_mode((width, height))

# Draw background and blit to screen
bg = pygame.Surface(screen.get_size()).convert()
bg.fill([53, 101, 77])
screen.blit(bg, (0, 0))

# Deal out cards, including card at center of board.  NOTE: currently deals only one hand.
deck = dealer.Deck()
deck.shuffle()
p1deck = deck.deal(12)
p2deck = deck.deal(12)
ctrcard = deck.deal(1)

# Set up the game
cardarea = setup.draw_card_placeholders(screen)
ctrcardlist = setup.draw_center_card(ctrcard)
playcount = 0
moves = 0
round_over = False

# Label and draw player decks
font = pygame.font.Font(None, 28)
text = font.render("Player 1", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.x, textpos.y = 750, 100
screen.blit(text, textpos)

p1datadeck = setup.build_datadeck(p1deck, (800, 200))
p2datadeck = setup.build_datadeck(p2deck, (800, 600))

#Render the first images in deck
screen.blit(p1datadeck[0][2], (p1datadeck[0][1].x, p1datadeck[0][1].y))
screen.blit(p2datadeck[0][2], (p2datadeck[0][1].x, p2datadeck[0][1].y))

# Event loop
while not round_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("debug: mouse click")
                mouse_pos = pygame.mouse.get_pos()
                cardareacounter = 0
                for card in cardarea:
                    if card.collidepoint(mouse_pos):
                        print(f'debug: collision at {card}')
                        # TODO: check if valid move?
                        moveloc = card.x, card.y
                        screen.blit(p1datadeck.pop(0)[2], moveloc)
                        screen.blit(p1datadeck[0][2], (p1datadeck[0][1].x, p1datadeck[0][1].y))

    # # P1
    # play_card('P1', p1deck, round)
    # # print('adding move')
    # moves += 1
    #
    # # P2
    # play_card('P2', p2deck, round)
    # # print('adding move')
    # moves += 1
    #
    # # Next round
    # # print('advance round')
    # round += 1
    # if round >= 12:
    #     round_over = True
    #     print('game over! final board:')
    #     draw_board()

    screen.blit(ctrcardlist[2], ctrcardlist[1])

    pygame.display.update()

if __name__ == '__main__': main()
