# Library imports
import pydealer as dealer
# pydealer is used to generate game objects.  Docs: https://pydealer.readthedocs.io/en/latest/usage.html#install-uninstall-with-pip

# Local imports
import setup
import cli_events as events

deck = setup.create_deck()
board = setup.create_board()

round_over = False
plays_on_board = 0
p1_played_cards = []
p2_played_cards = []

# Deal out cards, including card at center of board.
p1deck = deck.deal(12)
p2deck = deck.deal(12)
ctrcard = deck.deal(1)

while not round_over:
    # P1
    p1_played_cards.append(events.play_card(board, 'p1', p1deck.get(0)))

    # P2
    p2_played_cards.append(events.play_card(board, 'p2', p2deck.get(0)))

    # End the game when 24 cards are played
    if plays_on_board>=24:
        round_over = True
        print('game over! ')
        print('turn over center card...')
        print('final board:')
        draw_board()
        # Note: counting scores will be hard in CLI version!