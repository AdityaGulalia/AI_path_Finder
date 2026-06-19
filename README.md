# AI Path Finder

## Why I Built This 

I wanted to learn the foundations of AI and Reinforcement Learning by building something instead of following tutorials. The goal was not to create a complete racing simulator, but to understand how environments, agents, states, and actions work in practice.

This project started as a simple grid with walls and eventually became a small simulation environment where an agent can move around the track.

---

## What It Does

* Creates a grid-based track using NumPy
* Stores and validates car positions
* Prevents movement through walls
* Uses an action-based movement system (UP, DOWN, LEFT, RIGHT)
* Renders the environment in both machine-readable and human-readable forms
* Includes a random agent that can move around the environment
* Has unit tests for the main components

---

## Project Structure

### Track

The Track is responsible for storing the environment and answering questions such as:

* Is this position valid?
* Is this position a wall?

### Car

The Car only knows about its own position. It can propose a move, but it does not decide whether that move is allowed.

### Simulation

The Simulation coordinates everything. It translates actions into movement, checks collisions, updates the car's position, and handles rendering.

---

## Biggest Lessons Learned

### Separating Responsibilities Matters

One of the biggest lessons was learning that each class should have a clear job.

Instead of letting the car move itself immediately, the car proposes a move and the simulator decides whether the move is valid. This made the code cleaner and closer to how real simulations work.

### NumPy Coordinates vs Simulation Coordinates

I spent a lot of time understanding why:

```python
grid[y, x]
```

is used internally while the rest of the project works with:

```python
(x, y)
```

This helped me understand how arrays are stored and how coordinate systems are mapped in simulations.

### Testing Is About Behavior

Initially I was only testing function calls. During the project I learned that good tests verify behavior and state changes.

For example:

* Did the move succeed?
* Did the car actually end up in the correct position?
* Did the car stay in place when it hit a wall?

### Simulations Are Built Around States and Actions

Before this project, terms like "state", "action", and "environment" felt abstract.

After building the simulation, these concepts became much clearer:

* State = current environment configuration
* Action = movement choice
* Environment = track + rules
* Transition = moving from one state to another

---

## What I Learned

### Simulation Design

* State transitions
* Action systems
* Environment architecture
* Rendering and observations
* Agent-environment interaction

## Final Thoughts

This project achieved its goal. It helped me move beyond simple scripts and think more like a software engineer while also introducing the building blocks that appear in AI and Reinforcement Learning systems.

The next step is to focus on NumPy, Pandas, machine learning, and eventually neural networks and reinforcement learning.
