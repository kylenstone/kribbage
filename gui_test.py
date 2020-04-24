import pygame, sys
import os
from pygame.locals import *

# Initialize screen
pygame.init()
pygame.display.set_caption("Killer Kribbage!")
width = 1100
height = 800
screen = pygame.display.set_mode((width, height))

# Declare color variables
BLACK = (0, 0, 0)

# Draw background and blit to screen
bg = pygame.Surface(screen.get_size()).convert()
bg.fill([53, 101, 77])
screen.blit(bg, (0, 0))


# Draw 25 cardareas on the board
# Currently throws error: IndexError: list index out of range
cardarea = []
y_pos = 200
for x in range(5):
    for y in range(5):
            cardarea.append(pygame.draw.rect(screen, BLACK, [(x+1)*120, (y+1)*120, 75, 108], 1))
            y_pos+=120

# Draw flipped card in center of board
ctrcard = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'card_back.png')),
                                  (75, 108)).convert()
ctrcardrect = ctrcard.get_rect()
ctrcardrect.x = 360
ctrcardrect.y = 360

def load_image(name):
    # loads image from os dir and returns image object
    fullname = os.path.join('assets', 'name')
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image')
        raise SystemExit(message)
    return image, image.get_rect()

def place_card(card):
    return



# Event loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                print("mouse event")
    #           check if valid move?
    #           deck.handle_click(mouse_pos)
    #           play_card(pos)

    screen.blit(ctrcard, ctrcardrect)

    pygame.display.update()

if __name__ == '__main__': main()
