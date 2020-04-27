import pytest
import pydealer
import game_events as events
import game_setup as setup
import pygame

def test_build_deck():
    # Uses pygame to build a simple deck
    testdeck = pydealer.Deck()
    testhand = testdeck.deal(4)
    assert len(testhand) == 4
    assert testhand[0] != testhand[1]

def test_build_datadeck():
    # Should return a datadeck obj with three items: orig. deck, rect, Surface
    # TODO: currently fails on "SystemExit: cannot convert without pygame.display initialized"
    # Would a fixture be used to initialize pygame.display?
    testdeck = pydealer.Deck()
    testhand = testdeck.deal(4)
    pygame.init()
    pygame.display.set_mode((680, 480))
    testdatadeck = setup.build_datadeck(testhand)
    assert len(testdatadeck) == 4
    assert len(testdatadeck[0]) == 3
    assert type(testdatadeck[0][0]) == pydealer.card.Card
    assert type(testdatadeck[0][1]) == pygame.Rect
    assert type(testdatadeck[0][2]) == pygame.Surface

def test_play_turns():
    p1hand = testdeck.deal(12)
    p2hand = testdeck.deal(12)
