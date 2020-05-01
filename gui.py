import pydealer as dealer
# pydealer is used to generate game objects.  Docs: https://pydealer.readthedocs.io/en/latest/usage.html#install-uninstall-with-pip
import pygame
from pygame.locals import *
import os, sys
import game_events as events
import game_setup as setup

screen = setup.initialize_screen()

# Deal out cards, including card at center of board.
deck = dealer.Deck()
deck.shuffle()
p1deck, p2deck = setup.create_hands(deck, (12, 12))
center_card = deck.cards[0]
center_pygamecard = setup.PygameCard(center_card, (360, 360))

# Define some Board and Round state stuff
playcount = 0
moves = 0
used_moves = []
p1turn = True
round_over = False
game_over = False

# Display round setup cards on screen
board = setup.render_starting_board(screen, setup.create_board())
flat_board = setup.flatten_matrix(board)
draw_center_card = setup.render_card(screen, center_pygamecard.card, center_pygamecard.loc, face_up=False)

p1hand = setup.build_pygame_hand(p1deck, (800, 200))
p2hand = setup.build_pygame_hand(p2deck, (800, 600))

# Render P1 and P2 labels to screen
font = pygame.font.Font(None, 28)
p1label = font.render("Player 1", 1, (10, 10, 10))
p2label = font.render("Player 2", 1, (10, 10, 10))
screen.blit(p1label, (750, 100))
screen.blit(p2label, (750, 500))

# Render P1 and P2 decks to screen
draw_p1hand = setup.render_card(screen, p1hand[0].card, (800, 200))
draw_p2hand = setup.render_card(screen, p2hand[0].card, (800, 600))

# Event loop
while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                print(f'debug: {mouse_pos}')
                for spot in flat_board:
                    if spot.rect.collidepoint(mouse_pos):
                        print(f'debug: {spot.rect.collidepoint(mouse_pos)}')
                        print("click action w/ collision")
                        if events.check_valid_play(flat_board, spot):
                            print(f'click action: playing card at {spot}')
                            moveloc = spot.rect.x, spot.rect.y
                            if p1turn:
                                played_card = p1hand.pop(0)
                                setup.render_card(screen, played_card, moveloc)
                                #TODO: when using pop() we may need to update other data structures too
                                if len(p1hand) > 0:
                                    setup.render_card(screen, p1hand[0], p1hand[0].rect)
                                p1turn = False
                            else:
                                played_card = p2hand.pop(0)
                                setup.render_card(screen, played_card, moveloc)
                                if len(p2hand) > 0:
                                    setup.render_card(screen, p2hand[0], p2hand[0].rect)
                                else:
                                    round_over = True
                                p1turn = True
                            spot.is_open=False  # Set is_card_played_here to True
                            # print('Your turn P1') if p1turn else ('Your turn P2')
                            # print(f'debug: P1 cards left: {len(p1hand)}')
                            # print(f'debug: P2 cards left: {len(p2hand)}')
        if round_over:
            print("End of round")

    pygame.display.update()

if __name__ == '__main__': main()
