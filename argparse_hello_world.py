#!/usr/bin/env python3
"""
Program to finally get Argparse! :-)
"""
# Purpose: Say hello

import argparse

def get_args():
    """
    Well to process arguments!
    :return:
    """
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('-n','--name', metavar='name',
                        default='World', help='Name to Greet')
    return parser.parse_args()

def main():
    """
    Well this is the main function ya know!
    :return:
    """

    args = get_args()
    print('Hello, ' + args.name +'!')

if __name__ == '__main__':
    main()
