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
imported: 16 solution(s) in 6345 μs
running: all with benchmark
day1.part1: ~ (783 μs 12763 samples)
day1.part2: ~ (5014 μs 1995 samples)
day2.part1: ~ (422 μs 23672 samples)
day2.part2: ~ (696 μs 14358 samples)
day3.part1: ~ (3775 μs 2649 samples)
day3.part2: ~ (3212 μs 3114 samples)
day4.part1: ~ (1474 μs 6783 samples)
day4.part2: ~ (1660 μs 6025 samples)
day5.part1: ~ (288 μs 34654 samples)
day5.part2: ~ (4262 μs 2347 samples)
day6.part1: ~ (21 μs 468184 samples)
day6.part2: ~ (2563 ns 3592483 samples)
day7.part1: ~ (14 ms 697 samples)
day7.part2: ~ (14 ms 695 samples)
day8.part1: ~ (3155 μs 3170 samples)
day8.part2: ~ (24 ms 414 samples)
day9.part1: ~ (8533 μs 1172 samples)
day9.part2: ~ (8651 μs 1156 samples)
day10.part1: ~ (10 ms 991 samples)
day10.part2: ~ (35 ms 283 samples)
day11.part1: ~ (26 ms 381 samples)
day11.part2: ~ (30 ms 336 samples)
day12.part1: ~ (52 ms 191 samples)
day12.part2: ~ (772 ms 13 samples)
day13.part1: ~ (3243 μs 3083 samples)
day13.part2: ~ (4919 μs 2033 samples)
day14.part1: ~ (3915 μs 2555 samples)
day14.part2: ~ (1734 ms 6 samples)
day15.part1: ~ (2171 μs 4605 samples)
day15.part2: ~ (4322 μs 2314 samples)
day16.part1: ~ (8250 μs 1212 samples)
day16.part2: ~ (1811 ms 6 samples)
total: 4593 ms
```
