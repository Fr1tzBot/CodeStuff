#!/usr/bin/env python
"""fzf.py: a better fzf wrapper than https://github.com/JKubovy/fzf-wrapper"""

from subprocess import PIPE, run
from shutil import which

def hasFzf() -> bool:
    """Check if fzf is in PATH"""
    return which("fzf") is not None

def prompt(choices: list, fzfOpts: list=[]) -> list:
    """create an fzf prompt with the provided choices"""

    if choices is None or len(choices) == 0:
        raise ValueError("no fzf choices provided")

    if fzfOpts is None:
        raise ValueError("no fzf options provided")

    if not hasFzf():
        raise AttributeError("fzf does not appear to be installed")

    fzfOpts = ["fzf"] + fzfOpts

    print(fzfOpts)
    print( ("\n".join(choices)).encode().decode() )
    result = run(
        fzfOpts,
        input=(("\n".join(choices)).encode()),
        stderr=PIPE,
        stdout=PIPE,
        check=False
    )

    print(result.returncode)

    match result.returncode:
        case 0:
            return result.stdout.decode().strip().split('\n')
        case 1:
            return []
        case 130:
            return []
        case _:
            print(result.stderr)
            raise AttributeError(str(result.stderr.decode()))


print(prompt(["bobev", "is", "gay"]))
