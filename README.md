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
imported: 19 solution(s) in 23 ms
running: all with benchmark
day1.part1: ~ (793 μs 12605 samples)
day1.part2: ~ (4944 μs 2023 samples)
day2.part1: ~ (421 μs 23720 samples)
day2.part2: ~ (689 μs 14501 samples)
day3.part1: ~ (3650 μs 2740 samples)
day3.part2: ~ (3114 μs 3211 samples)
day4.part1: ~ (1467 μs 6814 samples)
day4.part2: ~ (1658 μs 6029 samples)
day5.part1: ~ (281 μs 35601 samples)
day5.part2: ~ (4162 μs 2403 samples)
day6.part1: ~ (21 μs 466999 samples)
day6.part2: ~ (2515 ns 3670491 samples)
day7.part1: ~ (14 ms 710 samples)
day7.part2: ~ (14 ms 707 samples)
day8.part1: ~ (3074 μs 3253 samples)
day8.part2: ~ (24 ms 422 samples)
day9.part1: ~ (8657 μs 1156 samples)
day9.part2: ~ (8718 μs 1148 samples)
day10.part1: ~ (9584 μs 1044 samples)
day10.part2: ~ (35 ms 290 samples)
day11.part1: ~ (26 ms 381 samples)
day11.part2: ~ (30 ms 339 samples)
day12.part1: ~ (50 ms 199 samples)
day12.part2: ~ (765 ms 14 samples)
day13.part1: ~ (3219 μs 3106 samples)
day13.part2: ~ (4803 μs 2083 samples)
day14.part1: ~ (3893 μs 2569 samples)
day14.part2: ~ (1725 ms 6 samples)
day15.part1: ~ (2206 μs 4534 samples)
day15.part2: ~ (4206 μs 2378 samples)
day16.part1: ~ (8060 μs 1241 samples)
day16.part2: ~ (1746 ms 6 samples)
day17.part1: ~ (1199 ms 9 samples)
day17.part2: ~ (4220 ms 3 samples)
day18.part1: ~ (215 ms 47 samples)
day18.part2: ~ (2719 ms 4 samples)
day19.part1: ~ (1519 μs 6583 samples)
day19.part2: ~ (2725 μs 3669 samples)
total: 13 s
```
