# Veil of Mysteries

*A Lord of the Mysteries–Themed Text RPG*

---

## Developer Info

**Name:** Kyle Pasag  
**Student Number:** A01428389  
**Course:** COMP 1510 — Programming Methods  
**Term Project**

---

## Game Description

You awaken within a mysterious 10×10 maze swallowed by gray fog.  
Your only chance of escape is to defeat three supernatural adversaries — each testing your mind in different ways.

Progress through the labyrinth, uncover eerie rooms, and survive strange encounters.  
Reach Level 3. Defeat the final Beyonder. Escape the fog.

Can you keep your sanity?

---

## How to Play — Quick Tutorial

| Action     | Input |
|------------|-------|
| Move Up    | `W`   |
| Move Down  | `S`   |
| Move Right | `D`   |
| Move Left  | `A`   |

🎯 Your objectives:

1. Explore the map and **find boss locations**
2. Win **Dice Duel**, **Wordle**, and **Anagram** minigames
3. **Level up** with each victory
4. Defeat the final foe before your **HP reaches 0**

Hints appear as you move — danger may appear randomly…

Press the wrong key? The game simply asks again.  
**Think carefully… each move matters.**

## Setup & Execution Instructions

### Requirements

- Python 3.13+ installed

### Running the Game

Open a terminal in the project folder and run:

Mac/Linux:

```bash
python3 game.py
```

Windows:

```bash
py game.py
```

---

## Project Requirements Compliance Table

| Requirement                                   | Where It Appears                              |
|-----------------------------------------------|-----------------------------------------------|
| Tuples used (immutable coords)                | `game_board.py` lines ~27                     |
| Dictionaries/lists used correctly             | `player.py`, `game_board.py`, `messages.py`   |
| Exceptions prevent crashes                    | `combat.py` lines ~245–249, `game.py` ~168    |
| No unnecessary global state                   | Verified                                      |
| Code decomposed into short reusable functions | Entire project (<15 lines each)               |
| Flat, readable structure                      | Verified in all modules                       |
| List comprehension used                       | `messages.py` line ~85                        |
| Dictionary comprehension used                 | `game_board.py` ~27                           |
| If-statements for decisions                   | `game.py` movement logic                      |
| Proper use of loops                           | Minigames in `combat.py`                      |
| Membership operator `in`                      | `combat.py` ~108, 166, 170                    |
| `range()` used appropriately                  | Wordle loop — `combat.py` line ~166           |
| `itertools.cycle()` used                      | Boss dialog cycling — `messages.py` line ~125 |
| Random module for encounters                  | `combat.py` boss events & dice rolls          |
| Function annotations included                 | In all functions                              |
| Doctests included for returning functions     | Verified                                      |
| All output formatted using f-strings          | Verified throughout                           |
| No single-letter variable names               | Verified across codebase                      |

