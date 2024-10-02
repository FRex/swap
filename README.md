# swap

A simple Python script that takes 2 filenames and swaps those files using
`os.rename` and then updates their modification times using `os.utime`.

My use case was to edit a file, and then swap it with the original,
recompile, and retest my program.

The same can be acomplished with `git stash` and `git stash pop`, but that
takes two commands instead of always the same one, affects other files in repo
by default, and does more disk writes than necessary.

The update of modification times is to force build systems (make, ninja) to
recompile the given file.
