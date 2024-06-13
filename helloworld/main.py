"""Top-level implementation of the helloworld program."""

import argparse
import sys
import time

import helloworld


parser = argparse.ArgumentParser(
        description='A simple example program to print a friendly greeting.')
parser.add_argument('--version', action='version',
        version='helloworld ' + helloworld.__version__)
parser.add_argument('--sleep', type=float, default=1, help="Seconds to sleep")
parser.add_argument('--exit_code', type=int, default=0, help="code to exit with")


def main(argv=None):
    if argv is None:
        argv = sys.argv

    args = parser.parse_args(argv[1:])

    print("Hello, world")
    print(f'Sleeping for {args.sleep} seconds')
    time.sleep(args.sleep)
    print("Goodbye")

    return args.exit_code
