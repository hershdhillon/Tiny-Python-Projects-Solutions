#!/usr/bin/env python3
"""Jumper"""

import argparse

def get_args():
    """Get Command Line Arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game Items')
    parser.add_argument('number', metavar='str', nargs='+', help='Dial Number')

    return parser.parse_args()


def main():
    """
    Converts passed numeric arguments into jumped numbers.
    """
    args = get_args()
    dial_number = args.number

    jumper_dictionary = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
                         '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    final_str = ''
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    for i in str(dial_number):
        if i in numbers:
            for key, value in jumper_dictionary.items():
                if i == key:
                    final_str += value
        else:
            final_str += i

    result = str(final_str).strip("[]")

    non_required = ["'", ","]

    new_char = ''

    for i in str(result):
        if i in non_required:
            pass
        else:
            new_char += i

    print(new_char)


if __name__ == '__main__':
    main()
