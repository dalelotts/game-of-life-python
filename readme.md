# Conway's Game of Life

## Rules

The universe of the Game of Life is an **infinite**, two-dimensional orthogonal grid of square cells,
each of which is in one of two possible states, alive or dead, (or populated and unpopulated, respectively).

Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.

At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbors dies, as if by under population.
1. Any live cell with two or three live neighbors lives on to the next generation.
1. Any live cell with more than three live neighbors dies, as if by overpopulation.
1. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

_nota bena:_ These are some mistakes I see in other implementations:

1. The universe of the game is **infinite** so you will likely run out of memory tracking both live and dead cells.
1. The universe cannot be represented in a two-dimensional array because negative array indexes are not supported (having a hard lower bounds of [0, 0] is not infinite)

## Set up

Set up the project environment by running the following:

```
python -m venv .venv
source .venv/bin/activate
make install
```

`make test` to run the tests

`make start` to run the game using an simple starting pattern.

`./main.py -h` for help.

## Implementation

- Test-Driven Development
- 100% code coverage (The TDD default - main.py is excluded)
- Infinite grid (at least to the extent it is addressable by the Point class)
- No `if` statements
- Immutable (state within the Game is mutated internally)
- No variable reassignments
- No naked primitives
- Short functions only
