#!/bin/env python3

import importlib
import pathlib
import heapq
import time
import argparse
import sys
import datetime

def display_time(t):
    if t == 0:
        return "0 s"
    elif t < 10e-6:
        return f"{t*1e+9:.0f} ns"
    elif t < 10e-3:
        return f"{t*1e+6:.0f} \u03bcs"
    elif t < 10:
        return f"{t*1e+3:.0f} ms"
    return f"{t:.0f} s"

def run_part(part, source, bench):
    if source is None:
        return "missing source", 0, 0
    elif part is None:
        return "missing implementation", 0, 0

    total = 0
    start = time.time()
    samples = 0
    while (samples==0 or bench) and time.time() - start < 2.0:
        t1 = time.time()
        res = part(source)
        t2 = time.time()
        total += t2 - t1 
        samples += 1
    return str(res), total / samples, samples

def print_part(nr, part, output, t, s, hide):
    time_display = display_time(t) + (f" {s} samples" if s > 1 else "")
    output_disp = "~" if hide else output
    if "\n" not in output_disp:
        print(f"day{nr}.part{part}: {output_disp} ({time_display})")
    else:
        print(f"day{nr}.part{part} ({time_display}):\n{output_disp}")

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("--all", "-a", action="store_true") 
    parser.add_argument("--days", "-d", nargs="+", type=int)
    parser.add_argument("--bench", "-b", action="store_true")
    parser.add_argument("--hide", action="store_true")
    args = parser.parse_args()

    run_all = args.all
    run_days = args.days
    run_bench = args.bench
    hide_res = args.hide

    if run_days and run_all:
        print("can't specify both specific days and all days", file=sys.stderr)    
        sys.exit(1)

    run_today = (not run_days) and (not run_all)
    if run_today:
        utcoffset = -datetime.timedelta(hours=5)
        timezone  = datetime.timezone(utcoffset)
        today     = datetime.datetime.now(tz=timezone)
        month     = today.month
        day       = today.day

        if month != 12 or day > 25:
            print("today is not during AoC", file=sys.stderr)
            sys.exit(1)

        run_days = [day]

    wd = pathlib.Path(".").absolute()
    days = []
    t1 = time.time()
    for file in wd.glob("day*.py"):
        module_name = file.stem
        day_nr = int(module_name[3:])
        day = importlib.import_module(module_name)
        heapq.heappush(days, (day_nr, day))
    t2 = time.time()

    print(f"imported: {len(days)} solution(s) in {display_time(t2-t1)}")
    if run_today: print(f"running: today ({run_days[0]})", end="")
    elif run_all: print("running: all", end="")
    else: print(f"running:", " ".join(map(str, run_days)), end="")
    print(" with benchmark" if run_bench else "") 

    total = 0
    while days:
        nr, day = heapq.heappop(days)
        
        if not run_all and nr not in run_days:
            continue

        source_path = pathlib.Path("input") / f"day{nr}.txt"
        if source_path.exists():
            with open(source_path) as fp:
                source = fp.read()
        else:
            source = None

        if "part1" in dir(day):
            part1 = day.part1
        else:
            part1 = None

        if "part2" in dir(day):
            part2 = day.part2
        else:
            part2 = None
        
        p1r, p1t, p1s = run_part(part1, source, run_bench)
        print_part(nr, 1, p1r, p1t, p1s, hide_res)
        p2r, p2t, p2s = run_part(part2, source, run_bench)
        print_part(nr, 2, p2r, p2t, p2s, hide_res)

        total += p1t + p2t 
    print(f"total: {display_time(total)}")
