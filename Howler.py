import sys
import os
import argparse
import io


def get_args():
    """
    Purpose: Parse the arguments.
    """
    parser = argparse.ArgumentParser(description='Howler', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', metavar='text', type=str, help='Input string or file.')
    parser.add_argument('-o', '--outfile', help='Output Filename', metavar='str', default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    else:
        args.text = io.StringIO(args.text + '\n')

    return args

def main():
    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    for line in args.text:
        out_fh.write(line.upper() + '\n')
    out_fh.close()

if __name__ == '__main__':
    main()
