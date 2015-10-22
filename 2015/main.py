#!/usr/bin/python

import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='MinnowBoard Bot')
    parser.add_argument('-m', '--modules', help='Modules Mode')
    parser.add_argument('-p', '--project', help='Project Mode')
    args = parser.parse_args()

    if args.modules == 'hello':
        print 'Hello'

# End of File
