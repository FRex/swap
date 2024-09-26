#!/usr/bin/env python3
import hashlib
import time
import sys
import os


# TODO: hashlib and time could be removed from imports in theory
# TODO: add doc strings and fix all TODOs


def makename(extraitems):
    # TODO: place this filename in directory of one of the files being swapped
    items = (time.time(), os.getpid(), extraitems)
    return hashlib.sha512(str(items).encode("UTF-8")).hexdigest()[:60] + ".tmp"


def main():
    # TODO: cmdline syntax to swap entire groups not just 2 files
    if len(sys.argv) != 3:
        print("Need 2 filenames", file=sys.stderr)
        sys.exit(1)

    fname1, fname2 = sys.argv[1], sys.argv[2]
    okay = True
    if not os.path.exists(fname1):
        print(f"{fname1} does not exist", file=sys.stderr)
        okay = False

    if not os.path.exists(fname2):
        print(f"{fname2} does not exist", file=sys.stderr)
        okay = False

    if not okay:
        sys.exit(2)

    tempname = makename((fname1, fname2))

    # TODO: fallbacks (behind a cmdline option) for swapping across filesystems
    # TODO: handle FileExistsError and other exceptions
    # TODO: retry in case tempname is occupied
    os.rename(fname1, tempname)
    os.rename(fname2, fname1)
    os.rename(tempname, fname2)


if __name__ == "__main__":
    # main()
    pass
