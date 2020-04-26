import pydealer as dealer
import pygame
from pygame.locals import *
import os, sys
import game_events as events
import game_setup as setup

# Instantiate the game

round_over = False
round = 0
moves = 0


# Deal out cards, including card at center of board.
deck = dealer.Deck()
deck.shuffle()
p1deck = deck.deal(12)
p2deck = deck.deal(12)
ctrcard = deck.deal(1)

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

# Set up the game
cardarea = setup.draw_card_placeholders(screen)
ctrcardlist = setup.draw_center_card(ctrcard)


# Label and draw player deck
font = pygame.font.Font(None, 28)
text = font.render("Player 1 deck - click board to place card", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.x, textpos.y = 750, 100
screen.blit(text, textpos)

p1deckrect = Rect(800, 200, 75, 108)
p1deckimg = pygame.transform.scale(pygame.image.load(os.path.join('assets/cards', '2_clubs.png')),
                                    (75, 108)).convert()



p1decklist = []
loop_pos = 0
for card in p1deck:
    tempimg, temprect = setup.load_image(p1deck[loop_pos])
    p1decklist.append((p1deck[loop_pos], temprect, tempimg))
    loop_pos+=1

# Event loop
while not round_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("debug: mouse click")
                mouse_pos = pygame.mouse.get_pos()
                cardareacounter = 0
                for card in cardarea:
                    if card.collidepoint(mouse_pos):
                        print(f'debug: collision at {card}')
                        # TODO: check if valid move?
                        moveloc = card.x, card.y
                        screen.blit(p1decklist.pop()[2], moveloc)

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

    screen.blit(ctrcardlist[2], ctrcardlist[1])
    screen.blit(p1deckimg, p1deckrect)

    pygame.display.update()

if __name__ == '__main__': main()
