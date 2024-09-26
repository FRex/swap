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


def exit2onmissing(fnames):
    """Print all missing files from fnames list and do sys.exit(2) if any are missing."""
    missing = False
    for fname in fnames:
        if not os.path.exists(fname):
            missing = True
            print(f"{fname} does not exist", file=sys.stderr)
    if missing:
        sys.exit(2)


def main():
    # TODO: cmdline syntax to swap entire groups not just 2 files
    if len(sys.argv) != 3:
        print("Need 2 filenames", file=sys.stderr)
        sys.exit(1)

    fname1, fname2 = sys.argv[1], sys.argv[2]
    exit2onmissing((fname1, fname2))

    # TODO: fallbacks (behind a cmdline option) for swapping across filesystems
    # TODO: handle FileExistsError and other exceptions
    # TODO: retry in case tempname is occupied
    tempname = makename((fname1, fname2))
    os.rename(fname1, tempname)  # move file 1 to temporary place
    os.rename(fname2, fname1)  # now move file 2 to now free file 1 place
    os.rename(tempname, fname2)  # now move original file 1 from temp to file 2 place


if __name__ == "__main__":
    main()
