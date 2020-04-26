# Data representation for the board using a list generator
board = [[0] * 5 for i in range(5)]
board[2][2] = 'x'

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