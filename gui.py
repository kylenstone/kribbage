import pydealer as dealer
# pydealer is used to generate game objects.  Docs: https://pydealer.readthedocs.io/en/latest/usage.html#install-uninstall-with-pip
import pygame
from pygame.locals import *
import os, sys
import game_events
import game_setup as setup

screen = setup.initialize_screen()

# Deal out cards, including card at center of board.
deck = dealer.Deck()
deck.shuffle()
p1deck, p2deck, center_card = setup.create_hidden_hands(deck, (12, 12, 1))
center_card = center_card.get(0).pop() # Convert from deque to card

# Define some Board and Round state stuff
playcount = 0
moves = 0
used_moves = []
p1turn = True
round_over = False
game_over = False

cardarea = setup.draw_card_placeholders(screen)
center_card = setup.render_card(screen, center_card, (360, 360), face_up=0)

# p1datadeck = setup.build_datadeck(p1deck, (800, 200))
# p2datadeck = setup.build_datadeck(p2deck, (800, 600))

# Render P1 and P2 labels to screen
font = pygame.font.Font(None, 28)
p1label = font.render("Player 1", 1, (10, 10, 10))
p2label = font.render("Player 2", 1, (10, 10, 10))
screen.blit(p1label, (750, 100))
screen.blit(p2label, (750, 500))

# Render P1 and P2 decks to screen
p1_top_of_deck = p1deck.cards[0]
p1_deck_xy_location = 800, 200
p1_deck_surf = setup.render_card(screen, p1_top_of_deck, (p1_deck_xy_location))
p2_top_of_deck = p2deck.cards[0]
p2_deck_xy_location = 800, 600
p2_deck_surf = setup.render_card(screen, p2_top_of_deck, (p2_deck_xy_location))

# screen.blit(p1datadeck[0][2], (p1datadeck[0][1].x, p1datadeck[0][1].y))
# screen.blit(p2datadeck[0][2], (p2datadeck[0][1].x, p2datadeck[0][1].y))

# Event loop
while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                # print("debug: mouse click")
                # for card in cardarea:
                #     if card[0].collidepoint(mouse_pos):
                #         if game_events.check_valid_play(cardarea, card):
                #             print(f'debug: playing card at {card[0]}')
                #             moveloc = card[0].x, card[0].y
                #             if p1turn:
                #                 played_card = p1datadeck.pop(0)
                #                 if len(p1datadeck) > 0:
                #                     screen.blit(p1datadeck[0][2], (p1datadeck[0][1].x, p1datadeck[0][1].y))
                #                 p1turn = False
                #             else:
                #                 played_card = p2datadeck.pop(0)
                #                 if len(p2datadeck) > 0:
                #                     screen.blit(p2datadeck[0][2], (p2datadeck[0][1].x, p2datadeck[0][1].y))
                #                 else:
                #                     round_over = True
                #                 p1turn = True
                #             screen.blit(played_card[2], moveloc) #Blit played card to new location
                #             card[1] = True  # Set is_card_played_here to True
                #             print('Your turn P1') if p1turn else ('Your turn P2')
                #             print(f'debug: {cardarea}')
                #             print(f'debug: P1 cards left: {len(p1datadeck)}')
                #             print(f'debug: P2 cards left: {len(p2datadeck)}')
        if round_over:
            print("End of round")

    pygame.display.update()

if __name__ == '__main__': main()
