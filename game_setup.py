import os
import pygame
import pydealer


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

def create_hidden_hands(deck, hand_sizes):
    # This could be extended to support four players w/ 6 card deck each!
    hands = []
    for i in hand_sizes:
        hands.append(deck.deal(i))
    return hands


def draw_card_placeholders(screen):
    # Declare color variables
    BLACK = (0, 0, 0)
    # Draw 25 cardareas on the board.
    # Each cardarea is a list with two parts, its Rect shape and a bool tracking if play has happened here.
    cardarea = []
    y_pos = 200
    for x in range(5):
        for y in range(5):
            cardarea.append([pygame.draw.rect(screen, BLACK, [(x + 1) * 120, (y + 1) * 120, 75, 108], 1), False])
            y_pos += 120 # TODO - can I delete this?
    cardarea[12][1] = True # Disallow play at ctrcard
    return cardarea


def load_image(card):
    fullname = card.value.lower()+"_"+card.suit.lower()+".png"
    dirname = os.path.join('assets/cards', fullname)
    try:
        image = pygame.transform.scale(pygame.image.load(dirname),(75, 108)).convert()
    except pygame.error as message:
        print('Cannot load image')
        raise SystemExit(message)
    return image, image.get_rect()


def load_center_card_images(center_card):
    # Draws center card in center of playing board
    center_card_face = load_image(center_card)
    center_card_back = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'card_back.png')),
                                        (75, 108)).convert()
    return center_card_face, center_card_back


def render_center_card(screen, center_card):
    # @TODO This function should become generic "render_card"
    center_card_face, center_card_back = load_center_card_images(center_card)
    screen.blit(center_card_back, (360, 360))
    return center_card_face, center_card_back

def build_datadeck(deck, loc=None):
    # Takes a Deck() object and returns fully constructed datadeck
    datadeck = []
    loop_pos = 0
    try:
        if loc is None:
            loc = (0, 0)
        for card in deck:
            tempimg, temprect = load_image(deck[loop_pos])
            temprect.x, temprect.y = loc
            #  TODO Don't append list inside list - append different object
            #  Should be "datadeck[1].surface", "datadeck[1].rect"
            datadeck.append((deck[loop_pos], temprect, tempimg))
            loop_pos += 1
    except ValueError:
        print('debug: loc must be in (x,y) format')
    return datadeck