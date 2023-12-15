# AoC 2023 Solutions

Repo for 2023 AoC solutions.

## About `today.py`
CLI to download puzzle input.

This script does follow the [automation guidelines](https://www.reddit.com/r/adventofcode/wiki/faqs/automation) on the /r/adventofcode community wiki. Specifically:
- Outbound calls are throttled to every 15 minutes via a timestamp file stored in the user folder `$HOME/.cache/aoc_today_ts`
- Once inputs are downloaded, they are cached locally in `./inputs[/{year}]/day{day}.txt` (the script will never overwrite these files)
  - If you suspect your input is corrupted, you can manually request a fresh copy by deleting both `$HOME/.cache/aoc_today_ts` and `./inputs[/{year}]/day{day}.txt`
- The User-Agent header is set to this repo and my contact info.

## About `setup.sh`
Sets up a correct `venv` and installs all required packages. Will skip the setup and just activate if it already exists.

## Times
Output of running `./aoc.py --all --bench --hide --no-test`

```
imported: 15 solution(s) in 4516 μs
running: all with benchmark
day1.part1: ~ (791 μs 12640 samples)
day1.part2: ~ (5003 μs 1999 samples)
day2.part1: ~ (407 μs 24581 samples)
day2.part2: ~ (667 μs 14986 samples)
day3.part1: ~ (3699 μs 2704 samples)
day3.part2: ~ (3344 μs 2991 samples)
day4.part1: ~ (1476 μs 6772 samples)
day4.part2: ~ (1813 μs 5515 samples)
day5.part1: ~ (381 μs 26191 samples)
day5.part2: ~ (5758 μs 1737 samples)
day6.part1: ~ (24 μs 411421 samples)
day6.part2: ~ (3328 ns 2759612 samples)
day7.part1: ~ (17 ms 578 samples)
day7.part2: ~ (16 ms 645 samples)
day8.part1: ~ (3411 μs 2931 samples)
day8.part2: ~ (23 ms 434 samples)
day9.part1: ~ (9718 μs 1029 samples)
day9.part2: ~ (9490 μs 1054 samples)
day10.part1: ~ (12 ms 865 samples)
day10.part2: ~ (37 ms 271 samples)
day11.part1: ~ (30 ms 339 samples)
day11.part2: ~ (36 ms 276 samples)
day12.part1: ~ (65 ms 155 samples)
day12.part2: ~ (846 ms 12 samples)
day13.part1: ~ (3394 μs 2946 samples)
day13.part2: ~ (4997 μs 2001 samples)
day14.part1: ~ (4604 μs 2172 samples)
day14.part2: ~ (1977 ms 6 samples)
day15.part1: ~ (2306 μs 4335 samples)
day15.part2: ~ (4449 μs 2248 samples)
total: 3124 ms
```
