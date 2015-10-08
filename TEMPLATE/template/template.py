#!/usr/bin/env python
from __future__ import print_function

try: # Python 3
    from urllib.request import urlopen
    from urllib.parse import urlencode
except ImportError: # Python 2
    from urllib import urlopen, urlencode
import sys
import argparse

real_stdout = sys.stdout

def prompt(*args):
    old_stdout = sys.stdout
    try:
        sys.stdout = sys.stderr
        return raw_input(*args) if hasattr(__builtins__, "raw_input") else input(*args)
    finally:
        sys.stdout = old_stdout


def main():
    parser = argparse.ArgumentParser(prog="{name}")
    parser.add_argument("term", help="")
    args = parser.parse_args()
    return 0


if __name__ == "__main__":
    sys.exit(main())
