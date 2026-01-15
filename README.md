# Veil of Mysteries

Veil of Mysteries is a text-based Python RPG inspired by Lord of the Mysteries by Cuttlefish That Loves Diving. You explore a fog-covered 10×10 grid maze, trigger random encounters, and level up by winning fights so you can challenge three bosses and escape before your HP hits 0.

What makes it fun is the variety in the boss gates: instead of pure combat, each boss is tied to a different minigame (dice duel, Wordle-style guessing, and an anagram challenge). The project is also organized into clear modules (game loop, board/movement, player stats, combat/minigames, and message handling) and includes input validation to keep gameplay smooth.

## Key Features

- Grid-based exploration (10×10 maze)
- Three boss encounters gated by different minigames:
  - Dice duel
  - Wordle-style guessing
  - Anagram challenge
- Simple progression system (win encounters to level up)
- Input validation (re-prompts on invalid keys)
- Modular codebase split by responsibility (game loop, board, player, encounters, messages)

## Demo

Goal: reach Level 3, defeat all three bosses, and escape the fog before HP hits 0.

Controls:

| Action | Key |
|---|---|
| Up | `W` |
| Down | `S` |
| Left | `A` |
| Right | `D` |

## Getting Started

### Requirements

- Python 3.11+ (3.13 recommended)

### Run

Mac/Linux:

```bash
python3 game.py
```

Windows:

```bash
py game.py
```

## Project Structure

High-level overview (file names may vary depending on your layout):

- `game.py` - main game loop and input handling
- `game_board.py` - maze/grid representation and movement rules
- `player.py` - player stats, HP, leveling
- `combat.py` - encounters and minigame logic
- `messages.py` - game text, prompts, dialogue

## Roadmap

Planned upgrades to bring this from a course project to a portfolio project:

- Save/load support (JSON)
- Procedural maze generation with optional seeded runs
- Fog-of-war (only reveal visited tiles)
- More encounters, items, and balancing
- Automated tests + CI (pytest + GitHub Actions)
- Lint/type checks (ruff + pyright)

## Notes

This repository is maintained as a portfolio project. Academic submission details (course info, rubric mapping, etc.) are intentionally kept out of the main README to keep this page employer-focused.

## License
MIT License © 2026 Kyle Pasag. See the [LICENSE](LICENSE) file for details.

## Author

Kyle Pasag

