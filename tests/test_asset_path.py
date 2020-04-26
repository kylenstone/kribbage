import os

def test_asset_path():
    assert os.path.exists('assets/card_back.png')
    assert os.path.exists('assets/cards')
    # assert that cards has 52 files

# def test_load_images():