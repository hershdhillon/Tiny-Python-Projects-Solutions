#!/usr/bin/env python3
"""Picnic Game"""

import argparse


def get_args():
    """Get Command Line Arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game Items'
    )
    parser.add_argument('item', metavar='str', nargs='+', help='Item(s) to bring')
    parser.add_argument('-s', '--sorted', action='store_true', help='Sort the Items')

    return parser.parse_args()


def main():
    """Main Stuff Happens here!"""

    args = get_args()
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()

    bringing = ''

    if num == 1:
        bringing = items[0]

    elif num == 2:
        bringing = ' and '.join(items)

    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print('You are bringing {}.'.format(bringing))


if __name__ == '__main__':
    main()
