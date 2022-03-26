'''Conway's game of life.'''
from typing import Callable, Iterable, List, Tuple


class Game:
    '''Construct with a set of live cell, then call tick() for next generation.'''

    def __init__(self, *live_cells: tuple[int, int]):
        self._live_cells = [*live_cells]

    def tick(self):
        self._live_cells = _survivors(
            self._live_cells) + _new_cells(self._live_cells)

    @property
    def live_cells(self):
        return self._live_cells


_NEIGHBORS = {
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
}


def _survivors(live_cells: List[tuple[int, int]]):
    return list(filter(_has_neighbors(live_cells, 2, 3), live_cells))


def _has_neighbors(live_cells: Iterable[tuple[int, int]], *neighborCount: int):
    allowed_neighbor_count = [*neighborCount]

    def count_neighbors(cell: Tuple[int, int]):
        live_neighbors = _count_live_neighbors(cell, live_cells)
        return live_neighbors in allowed_neighbor_count

    return count_neighbors


def _to_neighbors(cell: Tuple[int, int]) -> Iterable[Tuple[int, int]]:
    return map(
        lambda neighbor: (
            neighbor[0] + cell[0],
            neighbor[1] + cell[1]),
        _NEIGHBORS)


def _count_live_neighbors(
        cell: Tuple[int, int], live_cells: Iterable[Tuple[int, int]]):
    cells = list(live_cells)
    live_neighbors = filter(
        lambda neighbor: neighbor in cells,
        _to_neighbors(cell))

    return sum(1 for _ in live_neighbors)


def _to_dead_neighbors(
    live_cells: Iterable[Tuple[int, int]]
) -> Callable[[Tuple[int, int]], Iterable[Tuple[int, int]]]:
    cells = set(live_cells)

    def dead_neighbors(cell: Tuple[int, int]) -> Iterable[Tuple[int, int]]:
        return filter(
            lambda neighbor: neighbor not in cells,
            _to_neighbors(cell)
        )

    return dead_neighbors


def _new_cells(
        live_cells: Iterable[Tuple[int, int]]) -> Iterable[Tuple[int, int]]:
    dead_neighbors = set(_flat_map(_to_dead_neighbors(live_cells), live_cells))
    return list(filter(_has_neighbors(live_cells, 3), dead_neighbors))


def _flat_map(delegate, iteratable):
    result = []
    for member in iteratable:
        result.extend(delegate(member))
    return result
