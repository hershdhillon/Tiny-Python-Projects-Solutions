#!/usr/bin/env python3
"""
Purpose: Lookout for a narwhal and an octopus!
"""

import argparse

def get_args():
    """
    Purpose: Parse the arguments.
    """
    parser = argparse.ArgumentParser(description='CrowsNest')
    parser.add_argument('animal')
    return parser.parse_args()

def check_animal(animal_name):
    """
    Purpose: Finding ths first letter of the animal name.
    """
    first_letter = str.lower(animal_name[0])
    vowels = ['a','e','i','o','u']
    if first_letter in vowels:
        return True
    else:
        return False


def main():
    """
    Purpose: Replaces the preceding word depending on the vowel or consonant.
    """
    args = get_args()
    animal_name = str(args.animal)
    if check_animal(animal_name):
        print('Ahoy, Captain, an '+ animal_name + ' off the larboard bow!')
    else:
        print('Ahoy, Captain, a ' + animal_name + ' off the larboard bow!')


if __name__ == '__main__':
    main()
