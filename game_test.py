from pytest_unordered import unordered

from game import Game


def test_cell_with_no_neighbors_dies():
    expected_live_cells = []
    game = Game((0, 0))

    game.tick()

    actual = game.live_cells
    assert actual == expected_live_cells


def test_cell_with_one_live_neighbor_inc_column_dies():
    expected_live_cells = [(0, 0)]

    game = Game(
        *expected_live_cells,
        (0, 1),
        (0, -1)
    )

    game.tick()

    actual = game.live_cells
    assert all(elem in actual for elem in expected_live_cells)


def test_cells_with_three_live_neighbors_survive():
    expected_live_cells = [(0, 0), (-1, 1), (0, 1)]
    game = Game(
        (1, -1),
        *expected_live_cells,
    )

    game.tick()

    actual = game.live_cells

    assert all(elem in actual for elem in expected_live_cells)


def test_cell_with_two_live_neighbors_survives():
    expected_live_cells = [(0, 0)]
    game = Game(
        (-1, 1),
        *expected_live_cells,
        (1, -1)
    )

    game.tick()

    actual = game.live_cells

    assert actual == expected_live_cells


def test_dead_cell_with_three_live_neighbors_is_born():
    expected_live_cells = [
        (0, 0),
        (-1, 1),
        (0, 1),
        (-1, 0),
    ]

    game = Game(
        (-1, 1),
        (0, 1),
        (-1, 0)
    )

    game.tick()

    actual = game.live_cells

    assert actual == unordered(expected_live_cells)
