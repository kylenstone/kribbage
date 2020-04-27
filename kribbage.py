import pydealer as dealer
# pydealer is used to generate game objects.  Docs: https://pydealer.readthedocs.io/en/latest/usage.html#install-uninstall-with-pip

import string

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
# cardsinplay = p1deck + p2deck + ctrcard # Could be useful for debugging, make sure cards are properly randomized?

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

while not round_over:
    # P1
    play_card('P1', p1deck, round)
    # print('adding move')
    moves += 1

    # P2
    play_card('P2', p2deck, round)
    # print('adding move')
    moves += 1

    # Next round
    # print('advance round')
    round+=1
    if round>=12:
        round_over = True
        print('game over! final board:')
        draw_board()