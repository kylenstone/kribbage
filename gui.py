# Library imports
import pydealer as dealer # pygame generates card objects
import pygame # pygame creates the GUI
from pygame.locals import *
import os, sys

# Local imports
import game_events as events
import game_setup as setup

#Initialize pygame
screen = setup.initialize_screen()

# Deal out cards, including card at center of board.
deck = dealer.Deck()
deck.shuffle()
p1deck, p2deck = setup.create_hands(deck, (12, 12))
p1hand = setup.build_pygame_hand(p1deck, (800, 200))
p2hand = setup.build_pygame_hand(p2deck, (800, 600))

# Add a card to center of board
temp = deck.get(0).pop() # Gets card from deck, converts from deque to card
card_in_board_center = setup.PygameCard(temp, (360, 360))


# Define Board and Round state stuff
play_history = [] # TODO actually use this
p1turn = True
round_over = False
game_over = False

# Initialize the round's cards on screen
board = setup.render_starting_board(screen, setup.create_board())
render_center_card = setup.render_card(screen, card_in_board_center.card, card_in_board_center.loc, face_up=False)

# Render P1 and P2 labels to screen
font = pygame.font.Font(None, 28)
p1label = font.render("Player 1", 1, (10, 10, 10))
p2label = font.render("Player 2", 1, (10, 10, 10))
screen.blit(p1label, (750, 100))
screen.blit(p2label, (750, 500))

# Render P1 and P2 decks to screen
draw_p1hand = setup.render_card(screen, p1hand[0].card, (800, 200))
draw_p2hand = setup.render_card(screen, p2hand[0].card, (800, 600))

# Flatten 5x5 card matrix for easier use in game loop
flat_board = setup.flatten_matrix(board)

# Event loop
while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for spot in flat_board:
                    if spot.rect.collidepoint(mouse_pos):
                        if events.check_valid_play(flat_board, spot):
                            print(f'debug click action: playing card at {spot}')
                            moveloc = spot.rect.x, spot.rect.y
                            if p1turn:
                                played_card = p1hand.pop(0)
                                #TODO: when using pop() we may need to update other data structures too
                                setup.render_card(screen, played_card, moveloc)
                                if len(p1hand) > 0:
                                    setup.render_card(screen, p1hand[0], p1hand[0].rect)
                                p1turn = False
                            else:
                                played_card = p2hand.pop(0)
                                setup.render_card(screen, played_card, moveloc)
                                if len(p2hand) > 0:
                                    setup.render_card(screen, p2hand[0], p2hand[0].rect)
                                else:
                                    events.reveal_card_in_board_center(screen, card_in_board_center)
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
