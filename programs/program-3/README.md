# Wizard Shooty Game (By Carter Landry)

## Description
A simple arcade-style game featuring a Wizard, Spells, and a Spider.

- The Wizard can shoot spells with the `Space` key.
- If the Spider reaches the right edge of the screen, the Wizard loses a life.
- Hitting the Spider with a spell gives the Wizard a point.
- The game restarts automatically when all lives are lost.

## Features & Improvements
- **Randomized Spider Speeds** – The Spider respawns with a random speed for increased challenge.
- **Teleporting Spider Illusion** – When hit or after reaching the edge, the Spider respawns off-screen with a randomized position and delay.
- **Start Menu** – Added a start screen before gameplay begins.
- **Death Screen** – Displays a game-over message when all lives are lost. Press any key to restart.
- **Sound Effects** – Includes sounds for:
  - Firing a spell
  - Hitting the Spider
  - Losing a life

## How to Run
1. Make sure `pygame` is installed.
2. Navigate to the `src/` directory.
3. Run the game with:

```bash
python main.py
