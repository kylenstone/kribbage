# Killer Kribbage
"Killer Cribbage" is a favorite game of my family, played in almost all IRL holidays.  With #covid isolating everyone I thought it would be nice to build an online version of the game.

## Status
WIP:
- The game lacks a GUI entirely.
- Lacks support for two players operating independent clients.
- No networking (will follow after GUI)

### Testing
A suite of pytest tests will be written, but does not exist now.

### Assets
Card png images courtesy of https://code.google.com/archive/p/vector-playing-cards/

### Requirements
See `requirements.txt`
Python 3.7+
**Pygame must be installed for the game to work**

### Installation
Install python dependencies in a virtual environment:
```
python -m venv kribbage
source kribbage/bin/activate
```
If you also named your venv `kribbage`, `(kribbage)` should be prepended on your CLI. You can now use `pip` to install project dependencies, or use the `requirements.txt` install method.