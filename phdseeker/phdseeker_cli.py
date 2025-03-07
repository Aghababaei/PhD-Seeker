#!/usr/bin/env python3
"""
phdseeker

Usage:
    phdseeker -h
    phdseeker -V
    phdseeker [-k <keywords> -c <countries> --maxpage=<n> --output=<filetype(s)> -v]

options:
    -h --help                       Show this screen.
    -V --version                    Output version information, and repositories' list and exit.
    -v --verbose                    Show the found positions on the terminal.
    -k <keywords>, --keywords=<keywords>    Declare desired keywords to seek. [default: Computer Science, Machine Learning, Deep Learning]
    -c <countries>, --countries=<countries>    Filter by countries.
    -o <filetype(s)>, --output=<filetype(s)>     Set the output type csv/xlsx/both [default: both]
    --maxpage=<n>                   Maximum number of pages to fetch. [default: 10]
"""

import sys
from pathlib import Path
from threading import Thread
from time import perf_counter

import rich
from docopt import docopt

sys.path.append(
    Path(__file__).parent.parent.as_posix(),
)  # https://stackoverflow.com/questions/16981921
from phdseeker.main import PhDSeeker, checkNewVersion, Config
from phdseeker.constants import __version__


def main(args=docopt(__doc__)):
    if args["--version"]:
        rich.print(f"PhD-Seeker Version {__version__}")
        rich.print("\n>> Repositories included <<")
        for i, repo in enumerate(Config.repos().split(","), 1):
            c = Config(repo)
            rich.print(f"{i}. {repo:14}: ", end="")
            rich.print(c.baseURL)
        sys.exit()

    update = {"message": None}
    Thread(target=checkNewVersion, args=(update,), daemon=True).start()

    keywords = args["--keywords"]
    countries = args["--countries"]
    maxpage = int(args["--maxpage"])
    output = args["--output"]

    s = "s" if maxpage > 1 else ""
    incountries = f"in '{countries}' " if countries != None else ""
    rich.print(f"Searching for the Keywords '{keywords}' {incountries}up to {maxpage} page{s}.")
    s = perf_counter()
    ps = PhDSeeker(keywords, maxpage=maxpage, desired_countries=countries)
    ps.save(output)
    rich.print(f"Elapsed time is {perf_counter() - s:.2f}")

    if update["message"]:
        rich.print(update["message"])

    if args["--verbose"] and ps.sought_number:
        rich.print(ps)


if __name__ == "__main__":
    main(docopt(__doc__))
