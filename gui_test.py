import pydealer as dealer
import pygame
from pygame.locals import *
import os, sys

# Instantiate the game
deck = dealer.Deck()
deck.shuffle()
round_over = False
round = 0
moves = 0

# Data representation for the board using a list generator
board = [[0] * 5 for i in range(5)]
board[2][2] = 'x'

# Deal out cards, including card at center of board.
p1deck = deck.deal(12)
p2deck = deck.deal(12)
ctrcard = deck.deal(1)

def input_to_str(pos):
    col_pos = ord(pos[0].upper()) - 65 # Converts player input char A - E into int
    row_pos = int(pos[1])
    return col_pos, row_pos

def draw_board():
    # Draws the game as a 5x5 card matrix
    for l in board:
        print(l)

def play_card(player, deck, round):
    # Called each time p1 or p2 plays a card.
    player = player
    card = deck[round]
    play_success = False
    while not play_success:
        try:
            print(f'{player} Your card is: {card}')
            draw_board()
            pos = input('Enter card placement (Ex: A0,B4) >')
            col_pos, row_pos = input_to_str(pos)
            is_play_valid(col_pos, row_pos)
        except IndexError as error:
            print('Out of bounds. Play must be in format [A,B,C,D,E][0,1,2,3,4]')
        except AssertionError as error:
            print(error)
            print('Play was not in an available space. Try again')
        except ValueError as Error:
            print('Invalid input. Play must be in format \'A0\', etc.')
        else:
            board[col_pos][row_pos] = card
            play_success = True

def is_play_valid(col_pos, row_pos):
    # Each play must be on an open spot that is not the board center (pos[B2])
    col_pos = col_pos
    row_pos = row_pos
    assert board[col_pos][row_pos] == 0
    assert col_pos != 2 or row_pos != 2

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
cardarea = []
y_pos = 200
for x in range(5):
    for y in range(5):
            cardarea.append(pygame.draw.rect(screen, BLACK, [(x+1)*120, (y+1)*120, 75, 108], 1))
            y_pos+=120

# Draw flipped card in center of board
ctrcardimg = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'card_back.png')),
                                    (75, 108)).convert()
ctrcardrect = ctrcardimg.get_rect()
ctrcardrect.x, ctrcardrect.y = 360, 360
ctrcardlist = [ctrcard, ctrcardrect, ctrcardimg]

# Label and draw player1 deck
font = pygame.font.Font(None, 28)
text = font.render("Player 1 deck - click board to place card", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.x, textpos.y = 750, 100
screen.blit(text, textpos)

p1deckrect = Rect(800, 200, 75, 108)
p1deckimg = pygame.transform.scale(pygame.image.load(os.path.join('assets/cards', '2_clubs.png')),
                                    (75, 108)).convert()
def load_image(card):
    fullname = card.value+"_"+card.suit.lower()+".png"
    dirname = os.path.join('assets/cards', fullname)
    try:
        image = pygame.image.load(dirname).convert()
    except pygame.error as message:
        print('Cannot load image')
        raise SystemExit(message)
    return image, image.get_rect()

def place_card(card):
    return

p1decklist = []
loop_pos = 0
for card in p1deck:
    tempimg, temprect = load_image(p1deck[loop_pos])
    p1decklist.append((p1deck[loop_pos], temprect, tempimg))
    loop_pos+=1

# Event loop
while not round_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_pos = pygame.mouse.get_pos()
        #     if event.button == 1:
        #         print("mouse event")
        #         for area in cardarea:
        #             if cardarea[area].collidepoint(mouse_pos):
        #                 print("card goes here")
        #                 play_card(pos) - play card from hand to cardarea[area]
        #       check if valid move?

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

    screen.blit(ctrcardimg, ctrcardrect)
    screen.blit(p1deckimg, p1deckrect)

    pygame.display.update()

if __name__ == '__main__': main()
