![main_button_hovered](https://github.com/completelyblank/Terra-Incognita/assets/105001837/501cdb9a-7840-4d9d-84d1-35c8da6a19a3)

# Terra Incognita

## Overview
**Terra Incognita** is a simulation game where you play as Aiden Kors, an adventurer who possesses the unique ability to travel back in time. When Aiden dies, he regresses back in time, retaining knowledge of past events to make better decisions in subsequent attempts.

## Gameplay

### Movement
Aiden moves randomly (not user-controlled) in four directions: up, down, left, right.

### Encounters
- **Food**: Increases health.
- **Chests**: Grants stats such as strength, agility, and defense.
- **Monsters**: Engages in combat with the following outcomes:
  - **Win**: Gains experience and loses health based on the monster’s stats.
  - **Lose**: Death screen appears, and Aiden regresses back in time to retry.

## Mechanics

### Stack-Based Movement
Aiden’s movements are stored in a stack. If a move leads to death, it's popped, and another move is tried.

### Stage Completion
To complete a stage, Aiden must:
1. Level up 10 times.
2. Defeat all enemies.

## Technical Details

### Libraries Used
- **Pygame**: For game development.
- **Scikit-learn**: For machine learning algorithms.
- **Other Libraries**: As needed for additional functionalities.

## Features
- **Time Travel Mechanics**: Allows Aiden to retry after death with knowledge of past mistakes.
- **Randomized Movement and Encounters**: Ensures unique experiences in each playthrough.
- **Combat System**: Involves gaining experience and leveling up by defeating monsters.
- **Machine Learning**: Powers decision-making to optimize Aiden’s actions based on past experiences.
- **Custom Pixel Animations**: All pixel animations are created by myself.
- **Original Soundtrack (OST)**: The game's OSTs are my own creations.

## Implementation

### Initialization
1. Set up the game environment using Pygame.
2. Initialize Aiden’s stats, health, and movement stack.

### Movement Logic
1. Randomly move Aiden in one of the four directions.
2. Store each move in the stack.

### Encounter Handling
1. Detect encounters with food, chests, or monsters.
2. Update Aiden’s stats or engage in combat accordingly.

### Combat System
1. Calculate combat outcomes based on Aiden’s and the monster’s stats.
2. Update experience and health.

### Death and Regression
1. If Aiden dies, revert to a previous state using the movement stack.
2. Apply machine learning to avoid repeating fatal moves.

### Stage Completion
1. Check if Aiden has leveled up 10 times and defeated all enemies.
2. Progress to the next stage if criteria are met.
