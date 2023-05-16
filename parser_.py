import argparse
from typing import Union


class CapitalisedHelpFormatter(argparse.HelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = 'Usage: '
        return super(CapitalisedHelpFormatter, self).add_usage(
            usage, actions, groups, prefix)


def parse_args() -> Union[tuple[int, int], int]:
    parser = argparse.ArgumentParser(add_help=False, \
                                     formatter_class=CapitalisedHelpFormatter)
    parser._optionals.title = 'Options'

    parser.add_argument('-s', '--size',
                        help='Adjacency matrix size - number of vertices.',
                        required=True,
                        type=int)
    parser.add_argument('-n', '--number',
                        help='Number of tests for simulation process.',
                        required=True,
                        type=int)
    parser.add_argument('-m', '--manual',
                        help='If argument is provided, you will be asked to \
                            enter the adjacency matrix.',
                        required=False,
                        action='store_true')
    parser.add_argument('-v', '--verbose',
                        help='If argument is provided, more detailed output \
                              will be shown.',
                        required=False,
                        action='store_true')
    parser.add_argument('-t', '--timer',
                        help='If argument is provided, the time will be \
                          measured for each operation.',
                        required=False,
                        action='store_true')
    parser.add_argument('-h', '--help',
                        help='Show this help message and exit.',
                        default=argparse.SUPPRESS,
                        action='help')

    args = parser.parse_args()

    return args.size, args.number, args.manual, args.verbose, args.timer