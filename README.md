# ForFunsies

A collection of small Python projects I make for practice, experimentation, and because apparently learning Python is more fun when everything involves gremlins.

This repo is mostly me messing around with Python concepts, trying new things, breaking things, fixing them, and slowly turning simple ideas into unnecessarily elaborate projects.

---

## Projects

### `terminal_gremlin.py`

A chaotic terminal-based security clearance program that determines whether the user should be trusted.

Features include:

* User input and decision-making
* Risk / threat calculations
* Gremlin clearance levels
* Suspicion tracking
* Failed-attempt penalties
* Secret password challenge
* Randomized responses
* Questionable security practices
* A gremlin with authority it probably should not have

The program assigns a threat level based on the user's answers and behavior.

Results may include things such as:

* `APPROVED`
* `SUSPICIOUS`
* `PROBABLY FINE`
* `DO NOT TRUST`
* `GREMLIN DETECTED`

Accuracy not guaranteed.

Gremlin judgment is final.

---

### `gremlin_game.py`

What started as a simple Pygame movement test somehow became a tiny gremlin dungeon crawler inspired by Snake.

Control a gremlin worm with the arrow keys, collect loot, avoid dungeon walls, and survive long enough to escape.

#### Current Features

* Arrow-key movement
* Growing worm body
* Self-collision
* Dungeon wall collision
* Screen wrapping
* Multiple dungeon levels
* Different wall layouts for each level
* Loot requirements to unlock exits
* Locked and glowing dungeon doors
* Dungeon progression
* Death screen
* Victory screen
* Separate HUD so game information does not cover the dungeon
* Gremlin length tracker
* Total loot tracker
* Dungeon decorations
* Animated torches
* Stone floors and walls
* Moss, cracks, chains, bones, skulls, cobwebs, and treasure
* Tiny gremlin face with ears, eyes, and fangs

#### Loot

Normal food:

* Red Fruit — `+1 loot`
* Adds `+1` length

Rare food occasionally appears for a limited amount of time:

* Gold Fruit — `+5 loot`
* Purple Fruit — `+10 loot`
* Cursed Fruit — `+25 loot`
* Cursed Fruit also adds `+5` length

Yes, becoming five segments longer at once is part of the curse.

---

## Dungeon Levels

### Level 1 — Crypt Entrance

Collect enough loot to unlock the dungeon door and escape into the next area.

### Level 2 — Bone Halls

More walls.

More bones.

More opportunities to bonk directly into something.

### Level 3 — Cursed Vault

The final dungeon.

Survive, collect the required loot, and reach the exit to escape with everything you've stolen.

---

## Controls

| Key | Action                        |
| --- | ----------------------------- |
| `↑` | Move Up                       |
| `↓` | Move Down                     |
| `←` | Move Left                     |
| `→` | Move Right                    |
| `R` | Restart after death / victory |
| `Q` | Quit   (closes window)                       |

---

## Running the Projects

Make sure Python is installed.

Clone the repository or download the files, then open a terminal inside the project folder.

### Terminal Gremlin

Run:

```bash
py terminal_gremlin.py
```

### Gremlin Worm

The game uses Pygame Community Edition.

Install it with:

```bash
py -m pip install pygame-ce
```

Then run:

```bash
py gremlin_game.py
```

Even though the package is called `pygame-ce`, it is imported in Python using:

```python
import pygame
```

---

## Why This Repo Exists

Mostly for fun.

I'm learning Python and using this repo to experiment with things like:

* Variables
* User input
* Conditionals
* Loops
* Functions
* Lists
* Randomization
* Game logic
* Collision detection
* Timers
* GUI / game windows
* Pygame
* Debugging
* Gradually creating problems for myself and then figuring out how to fix them

The projects aren't meant to be serious production software.

They're here so I can learn by building things I actually enjoy making.

---

## Current Development Philosophy

1. Have an idea.
2. Write code.
3. Run code.
4. Receive error.
5. Stare at error.
6. Fix error.
7. Add one innocent little feature.
8. Accidentally create an entire dungeon system.
9. Repeat.

---

## Status

Still actively being messed with.

More gremlin-related nonsense will probably appear.
