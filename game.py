import pydealer as dealer
# pydealer is used to generate game objects.  Docs: https://pydealer.readthedocs.io/en/latest/usage.html#install-uninstall-with-pip
import pygame
from pygame.locals import *
import os, sys
import game_events
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
used_moves = []
p1turn = True
round_over = False
game_over = False

# Label and draw player decks
font = pygame.font.Font(None, 28)
p1label = font.render("Player 1", 1, (10, 10, 10))
p1textpos = p1label.get_rect()
p1textpos.x, p1textpos.y = 750, 100
p2label = font.render("Player 2", 1, (10, 10, 10))
p2textpos = p2label.get_rect()
p2textpos.x, p2textpos.y = 750, 500

screen.blit(p1label, p1textpos)
screen.blit(p2label, p2textpos)

p1datadeck = setup.build_datadeck(p1deck, (800, 200))
p2datadeck = setup.build_datadeck(p2deck, (800, 600))

#Render the first images in deck
screen.blit(p1datadeck[0][2], (p1datadeck[0][1].x, p1datadeck[0][1].y))
screen.blit(p2datadeck[0][2], (p2datadeck[0][1].x, p2datadeck[0][1].y))
screen.blit(ctrcardlist[2], ctrcardlist[1]) # render center card

# Event loop
while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                # print("debug: mouse click")
                for card in cardarea:
                    if card[0].collidepoint(mouse_pos):
                        if game_events.check_valid_play(cardarea, card):
                            print(f'debug: playing card at {card[0]}')
                            moveloc = card[0].x, card[0].y
                            if p1turn:
                                played_card = p1datadeck.pop(0)
                                if len(p1datadeck) > 0:
                                    screen.blit(p1datadeck[0][2], (p1datadeck[0][1].x, p1datadeck[0][1].y))
                                p1turn = False
                            else:
                                played_card = p2datadeck.pop(0)
                                if len(p2datadeck) > 0:
                                    screen.blit(p2datadeck[0][2], (p2datadeck[0][1].x, p2datadeck[0][1].y))
                                else:
                                    round_over = True
                                p1turn = True
                            screen.blit(played_card[2], moveloc) #Blit played card to new location
                            card[1] = True  # Set is_card_played_here to True
                            print('Your turn P1') if p1turn else ('Your turn P2')
                            print(f'debug: {cardarea}')
                            print(f'debug: P1 cards left: {len(p1datadeck)}')
                            print(f'debug: P2 cards left: {len(p2datadeck)}')
        if round_over:
            print("End of round")

    pygame.display.update()

if __name__ == '__main__': main()
