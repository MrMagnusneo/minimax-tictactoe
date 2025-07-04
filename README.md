# Tic-Tac-Toe with Minimax

## Overview
This Python implementation of Tic-Tac-Toe features an unbeatable AI opponent using the Minimax algorithm. The AI makes optimal decisions at every game state, guaranteeing that the best possible outcome for a human player is a draw.

## Features
- **Unbeatable AI** using Minimax algorithm with alpha-beta pruning principles
- **Strategic opening moves** based on game theory principles
- **Win/draw detection** after every move
- **Input validation** for player moves
- **Clean console interface** with board visualization

## Requirements
- Python 3.x

## Installation & Execution
1. Save a file named `tttui.py`
2. Run from the command line:
```bash
python tttui.py
```

## Game Instructions
1. Choose which side the computer will play:
   - Enter `1` for computer as X (goes first)
   - Enter `2` for computer as O (goes second)

2. Board positions are specified using a two-digit code:
   - First digit: row (0-2)
   - Second digit: column (0-2)
   ```
   00 | 01 | 02
   ---+----+---
   10 | 11 | 12
   ---+----+---
   20 | 21 | 22
   ```

3. When prompted, enter your move using the row-column format (e.g., `11` for center)

## AI Strategy
The AI employs a multi-layered approach:
1. **Opening moves**:
   - Always starts in a corner position
   - Takes center if player occupies corner
   - Creates fork opportunities when possible

2. **Mid/end-game**:
   - Immediate win detection
   - Player win blocking
   - Minimax algorithm for optimal decision making

The Minimax implementation recursively evaluates all possible game states to depth, scoring positions based on:
- +∞ for winning terminal states
- -∞ for losing terminal states
- 0 for draws
- Recursive evaluation of intermediate positions

## Code Structure
- `check_win()`: Evaluates board state for wins/draws
- `minimax()`: Recursive minimax implementation
- `bot_move()`: Decision logic combining heuristics and minimax
- `game()`: Main game loop and interface

## Technical Notes
1. The first computer move is always in a corner position (statistically optimal)
2. Special handling of first two moves reduces unnecessary minimax calls
3. The minimax algorithm evaluates approximately 5,000-10,000 states in mid-game positions
4. Board representation uses integer values:
   - 0: Empty
   - 1: X
   - 2: O

## Example Gameplay
```
Input computer team (1 -> X, 2 -> O): 2

Current board:
   |   |   
———|———|———
   |   |   
———|———|———
   |   | X

Possible moves:
00 01 02
10 11 12
20 21 22
Your move: 11

Current board:
   |   |   
———|———|———
   | O |   
———|———|———
   |   | X
...
Computer wins!
```
