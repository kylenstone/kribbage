import os
import pygame
import pydealer


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
            y_pos += 120
    cardarea[12][1] = True # Disallow play at ctrcard
    return cardarea

def draw_center_card(ctrcard):
    # Draw flipped card in center of board
    ctrcardimg = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'card_back.png')),
                                        (75, 108)).convert()
    ctrcardrect = ctrcardimg.get_rect()
    ctrcardrect.x, ctrcardrect.y = 360, 360
    ctrcardlist = [ctrcard, ctrcardrect, ctrcardimg]
    return ctrcardlist

def load_image(card):
    fullname = card.value+"_"+card.suit.lower()+".png"
    dirname = os.path.join('assets/cards', fullname)
    try:
        image = pygame.transform.scale(pygame.image.load(dirname),(75, 108)).convert()
    except pygame.error as message:
        print('Cannot load image')
        raise SystemExit(message)
    return image, image.get_rect()

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
            datadeck.append((deck[loop_pos], temprect, tempimg))
            loop_pos += 1
    except ValueError:
        print('debug: loc must be in (x,y) format')
    return datadeck