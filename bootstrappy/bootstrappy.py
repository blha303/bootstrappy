#!/usr/bin/env python
from __future__ import print_function

import shutil
import os
import argparse
import sys

real_stdout = sys.stdout

def prompt(*args):
    old_stdout = sys.stdout
    try:
        sys.stdout = sys.stderr
        return raw_input(*args) if hasattr(__builtins__, "raw_input") else input(*args)
    finally:
        sys.stdout = old_stdout


def do_format(file, args, curly=False):
    with open(os.path.expanduser(file.format(**args)), "r+") as f:
        contents = f.read()
        f.seek(0)
        if curly:
            f.write(contents.format(**args))
        else:
            f.write(contents % args)
    print("Formatted {}".format(os.path.basename(file.format(**args))), file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(prog="bootstrappy")
    parser.add_argument("name", help="Name of project")
    parser.add_argument("desc", help="Description of project")
    parser.add_argument("deps", help="Dependencies. Comma-separated list")
    args = vars(parser.parse_args())
    args["deps"] = repr(args["deps"].split(","))
    WORKSPACE_PATH = os.path.expanduser("~/workspace/{name}".format(**args))
    if not os.path.dirname(__file__):
        print("This program must be run as a module for reasons. Sorry.", file=sys.stderr)
        return 1
    if os.path.isdir(WORKSPACE_PATH):
        print("There is already a directory named {} in ~/workspace. Move that one, then try this again.".format(args.name), file=sys.stderr)
        return 2
    print("Copying {} to {}...".format("{}/../TEMPLATE".format(os.path.dirname(__file__)), WORKSPACE_PATH), file=sys.stderr)
    shutil.copytree("{}/../TEMPLATE".format(os.path.dirname(__file__)), WORKSPACE_PATH)
    print("Formatting setup.py...", file=sys.stderr)
    do_format("~/workspace/{name}/setup.py", args)
    print("Formatting README.md...", file=sys.stderr)
    do_format("~/workspace/{name}/README.md", args)
    print("Renaming module directory from template to {name}...".format(**args), file=sys.stderr)
    shutil.move(WORKSPACE_PATH + "/template".format(**args), WORKSPACE_PATH + "/{name}".format(**args))
    print("Formatting {name}/__main__.py...".format(**args), file=sys.stderr)
    do_format("~/workspace/{name}/{name}/__main__.py", args, curly=True)
    print("Formatting {name}/{name}.py...".format(**args), file=sys.stderr)
    do_format("~/workspace/{name}/{name}/{name}.py", args, curly=True)
    print("Renaming main file from {name}/template.py to {name}/{name}.py...".format(**args), file=sys.stderr)
    shutil.move(WORKSPACE_PATH + "/{name}/template.py".format(**args), WORKSPACE_PATH + "/{name}/{name}.py".format(**args))
    os.chdir(WORKSPACE_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
