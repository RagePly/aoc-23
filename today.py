#!/bin/env python3

import dotenv
import requests
import datetime
import time
import argparse
import sys
import os
import pathlib

class AocError(Exception): ...
def main() -> int: 
    dotenv.load_dotenv()

    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("--dry", action="store_true", help="only displays what endpoints will be called and files affected")
    parser.add_argument("-d", "--day", type=int, help="override the day")
    parser.add_argument("-y", "--year", type=int, help="overrid the year")
    args = parser.parse_args()

    is_dry = args.dry

    # check that requests are limited to once every 15-minutes
    cache_folder = pathlib.Path(os.getenv("HOME")) / ".cache"
    timestamp = cache_folder / "aoc_today_ts"

    if timestamp.exists():
        try:
            with open(timestamp, "r") as fp:
                ts = float(fp.read())
        except ValueError:
            raise AocError("timestamp file was incorrectly formatted")

        if time.time() - ts < 15 * 60:
            raise AocError("requests are limited to once every 15 minutes")
    else:
        cache_folder.mkdir(parents=True, exist_ok=True) 



    is_manual = args.year is not None or args.day is not None

    # Get the correct time
    utcoffset = -datetime.timedelta(hours=5)
    timezone  = datetime.timezone(utcoffset)
    today     = datetime.datetime.now(tz=timezone)
    year      = today.year if args.year is None else args.year
    month     = today.month if not is_manual else 12
    day       = today.day if args.day is None else args.day
    
    resolved_day = datetime.datetime(year=year, month=month, day=day, tzinfo=timezone)
    if today < resolved_day:
        raise AocError("can't fetch days in the future")

    if month != 12:
        raise AocError("It is not december yet...")

    base = pathlib.Path("input")
    if year != today.year: 
        base = base / str(year)
    path = base / f"day{day}.txt"

    if path.exists():
        raise AocError(f"this day has already been fetched, manually delete the file ({path}) to allow the script to fetch this day")

    if is_dry:
        print("new file:", str(path))
    else:
        base.mkdir(parents=True, exist_ok=True)
    
    if not "AOC_SESSION" in os.environ:
        raise AocError("missing session cookie (export AOC_SESSION=<session cookie> or place in .env")

    session = os.getenv("AOC_SESSION")
    headers = {
        "User-Agent": "https://github.com/RagePly/aoc-23/blob/master/today.py the.hugo.lom@gmail.com",
        "Cookie": f"session={session}"
    }

    endpoint = f"https://adventofcode.com/{year}/day/{day}/input"
    
    if is_dry:
        print("endpoint:", endpoint)
        print("header:")
        for n,v in headers.items():
            print(" ", n + ":", v)
    else:
        res = requests.get(endpoint, headers=headers)

        # write the timestamp independant of result
        with open(timestamp, "w") as fp:
            fp.write(str(time.time()))

        if not res.ok:
            raise AocError("failed to fetch puzzle input")
        
        content = res.text

        with open(path, "w") as fp:
            bs = fp.write(content)

        print(f"wrote {bs} to {path}")

    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except AocError as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)
