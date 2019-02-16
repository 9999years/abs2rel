#! /usr/bin/python3

import os.path
import sys

def main():
    if len(sys.argv) != 3:
        print('usage: abs2rel DEST START_DIR')
        sys.exit(1)
    _, dest, start = sys.argv
    print(os.path.relpath(dest, start=start))

if __name__ == '__main__':
    main()
