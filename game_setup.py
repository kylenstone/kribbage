# Library imports
import os
import pygame
from pydealer import card


class PygameCard:
    """
    takes a pydealer.card.Card and adds image and rect properties for use with pygame
    """
    def __init__(self, card, loc):
        self.card = card
        self.suit = card.suit
        self.value = card.value
        self.image = load_card_image(card)
        self.loc = loc
        self.rect = self.image.get_rect().move(loc)


class BoardSpot:
    """
    Spot on the board where a card can be played
    """
    def __init__(self, rect=None, is_open=True):
        self.is_open = is_open
        self.rect = rect


def initialize_screen():
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
    return screen


def load_card_image(card, face_up=True):
    # Associates images on disk with passed-in card.  Returns Surface object.
    if face_up is False:
        try:
            card_image = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'card_back.png')),(75, 108)).convert()
        except pygame.error as message:
            print('Cannot load image')
            raise SystemExit(message)
    else:
        try:
            fullname = card.value.lower() + "_" + card.suit.lower() + ".png"
            dirname = os.path.join('assets/cards', fullname)
            card_image = pygame.transform.scale(pygame.image.load(dirname), (75, 108)).convert()
        except pygame.error as message:
            print('Cannot load image')
            raise SystemExit(message)
    return card_image


def render_card(screen, card, loc, face_up=True):
    # passed card must be pygame.card.Card, loc must be tuple(x, y)
    rendered_image = load_card_image(card, face_up)
    screen.blit(rendered_image, loc)
    return rendered_image


def build_pygame_hand(hand, loc=(0,0)):
    # Takes a pygame.deck.Deck and object and returns a hand of pygamecards
    # Sets all cards to render at location
    pygamehand = []
    loop_pos = 0
    for card in hand:
            mycard = PygameCard(card, loc)
            pygamehand.append(PygameCard(mycard, loc))
    return pygamehand


def create_hands(deck, hand_sizes):
    # This could be extended to support four players w/ 6 card deck each!
    hands = []
    for i in hand_sizes:
        hands.append(deck.deal(i))
    return hands


def render_starting_board(screen):
    # Create the board object as 5x5 matrix using nested list comprehension
    board = [[BoardSpot() for j in range(5)] for i in range(5)]
    board[2][2].is_open = False # Disallow play at center spot

    # Declare color variables
    BLACK = (0, 0, 0)
    y_pos = 200

    # Run a throwaway loop to draw rects on board
    for x in range(5):
        for y in range(5):
            rect = pygame.draw.rect(screen, BLACK, [(x + 1) * 120, (y + 1) * 120, 75, 108], 1)
            board[x][y].rect = rect
            y_pos += 120
    return board


def flatten_matrix(matrix):
    # Flattens matrix into a list
    list = []
    for sublist in matrix:
        for val in sublist:
            list.append(val)
    return list