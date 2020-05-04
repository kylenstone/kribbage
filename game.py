# Library imports
import pydealer as dealer # pygame generates card objects
import pygame # pygame creates the GUI
from pygame.locals import *
import os, sys
import pygbutton

# Local imports
import game_events as events
import game_setup as setup

class KribbageGame:
    game_over = False

    """
    Game has players, rounds
    """
    def __init__(self, players):
        self.players = players


class Player:
    def __init__(self, name, hand=None, pygamehand=None):
        self.name = name
        self.hand = hand
        self.pygamehand = hand


class Round():
    round_over = False
    remaining_turns = 24
    p1turn = True

    def __init__(self, players, deck, hands, card_in_board_center, board):
        self.players = players
        self.board = board
        self.deck = deck
        self.hands = hands
        self.board = board
        self.card_in_board_center = card_in_board_center

    def play_turn(self, player, moveloc):
        print(f'debug click action: {player.name} playing card at {moveloc}')
        self.player = player
        self.moveloc = moveloc

        if r.remaining_turns > 0:
            # played_pycard = player.hand.cards.popleft()
            played_card = player.pygamehand.pop(0)
            setup.render_card(screen, played_card, moveloc)
            r.remaining_turns -= 1
            r.p1turn = not r.p1turn
            print(f'debug: p1 turn is now {r.p1turn}')
            print(r.remaining_turns)
            if len(player.pygamehand) > 0:
                setup.render_card(screen, player.pygamehand[0], player.pygamehand[0].rect)
        return # TODO Not sure what to return here.  played_card?


def create_players():
    p1name = "Kyle"
    p2name = "Kevin"
    # p1name = input("Enter first player's name: >")
    # p2name = input("Enter second player's name: >")
    p1 = Player(p1name)
    p2 = Player(p2name)
    return [p1, p2]


def initialize_round():
    """ Initializes a fresh round:
    - Creates board and renders it to screen
    - Deals a shuffled deck
    - Creates hands for p1, p2
    - Draws a card at center of board and renders it to screen
    - Instantiates the new round
    """
    board = setup.render_starting_board(screen)

    # Deal out cards, including card at center of board.
    deck = dealer.Deck()
    deck.shuffle()
    p1.hand, p2.hand = setup.create_hands(deck, (12, 12))
    p1.pygamehand = setup.build_pygame_hand(p1.hand, (800, 200))
    p2.pygamehand = setup.build_pygame_hand(p2.hand, (800, 600))
    # Add a card to center of board
    ctrcard = deck.get(0).pop()  # Gets card from deck, converts from deque to card
    card_in_board_center = setup.PygameCard(ctrcard, (360, 360))
    # Draw the center card
    render_center_card = setup.render_card(screen, card_in_board_center.card, card_in_board_center.loc, face_up=False)
    r = Round(game.players, deck, [p1.hand, p2.hand], card_in_board_center, board)
    return r

# Create players.
players = create_players()

# Instantiate the main game object.
game = KribbageGame(players)

# Give each Player an alias to refer to
p1 = game.players[0]
p2 = game.players[1]


# Main event loop
while not game.game_over:

    # Initialize pygame
    screen = setup.initialize_screen()

    # Initialize the round
    r = initialize_round()

    # Define Board and Round state stuff
    p1turn = True

    # Render P1 and P2 labels to screen
    font = pygame.font.Font(None, 28)
    p1label = font.render("Player 1", 1, (10, 10, 10))
    p2label = font.render("Player 2", 1, (10, 10, 10))
    screen.blit(p1label, (750, 100))
    screen.blit(p2label, (750, 500))

    # Render P1 and P2 decks to screen
    draw_p1hand = setup.render_card(screen, p1.hand[0], (800, 200))
    draw_p2hand = setup.render_card(screen, p2.hand[0], (800, 600))

    # Flatten 5x5 card matrix so we can use list-style iteration in game loop below
    flat_board = setup.flatten_matrix(r.board)

    while not r.round_over:  # TODO deal with this
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if r.remaining_turns > 0:
                    for spot in flat_board:
                        if spot.rect.collidepoint(mouse_pos):
                            if events.check_valid_play(spot):
                                moveloc = spot.rect.x, spot.rect.y
                                if r.p1turn:
                                    r.play_turn(p1, moveloc)
                                else:
                                    r.play_turn(p2, moveloc)
                                spot.is_open=False  # Set is_card_played_here to True
                else:
                    print('Time to reveal center card')
                    setup.render_card(screen, r.card_in_board_center.card, (360, 360), face_up=True)
                    button = pygbutton.PygButton((350, 50, 100, 40), 'Next Round')
                    button.draw(screen)
                    print('debug')
                    if button.rect.collidepoint(mouse_pos):
                        print("Clicked new round button")
                        # Start a new round
                        r.round_over = True
                        print('still here')
        # Event updater within round:
        pygame.display.update()
    # Event updater within game:
    pygame.display.update()