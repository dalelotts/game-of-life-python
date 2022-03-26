#!/usr/bin/env python3

import sys
from typing import Tuple
import argparse
import re

from terminaltables import AsciiTable

from game import Game

DELIMITERS = r'[ ;.]'


def main():
    argument_parser = argparse.ArgumentParser(epilog ="e.g. ./main.py -c 0,0 0,1 0,2 1,2 2,1")
    argument_parser.add_argument('-c',
                                '--live-cell',
                                action='extend',
                                type=_cell,
                                nargs='+',
                                help='<Required> x,y coordinates of living cells.',
                                required=True,
                                default=[]
                                )
    argument_parser.add_argument(
        '-v', '--version', action='version', version='%(prog)s 1.0')
    arguments = argument_parser.parse_args()

    game = Game(*arguments.live_cell)

    render(game.live_cells)

    prompt = "Press enter to see the next game state, or type exit to quit: "
    choice = input(prompt)
    while choice != "exit":
        game.tick()
        render(game.live_cells)
        choice = input(prompt)


def _cell(point: str):
    try:
        coordinates = re.split(DELIMITERS, point)[0]
        return tuple(map(int, coordinates.split(',')))

    except Exception as exception:
        raise argparse.ArgumentTypeError("cells must be x,y") from exception


def render(live_cells):

    if live_cells:
        game_grid = []

        start_column = min(map(lambda cell: cell[1], live_cells))
        end_column = max(map(lambda cell: cell[1], live_cells))

        start_row = min(map(lambda cell: cell[0], live_cells))
        end_row = max(map(lambda cell: cell[0], live_cells))

        game_grid.append(["-", *range(start_column, end_column + 1)])

        for row in range(end_row, start_row - 1, -1):
            columns = [row]
            for column in range(start_column, end_column + 1):
                content = "😀" if (row, column) in live_cells else "X"
                columns.append(content)

            game_grid.append(columns)

        ascii_table = AsciiTable(game_grid, "Conway's Game of Life")
        print(ascii_table.table)
        print()
    else:
        print("Oh no! All cells in the game are dead.")
        sys.exit()


if __name__ == '__main__':
    main()
