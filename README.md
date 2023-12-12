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
imported: 12 solution(s) in 5241 μs
running: all with benchmark
day1.part1: ~ (809 μs 12354 samples)
day1.part2: ~ (4975 μs 2010 samples)
day2.part1: ~ (414 μs 24149 samples)
day2.part2: ~ (682 μs 14655 samples)
day3.part1: ~ (3681 μs 2717 samples)
day3.part2: ~ (3233 μs 3093 samples)
day4.part1: ~ (1471 μs 6797 samples)
day4.part2: ~ (1665 μs 6004 samples)
day5.part1: ~ (285 μs 35089 samples)
day5.part2: ~ (4216 μs 2372 samples)
day6.part1: ~ (23 μs 432087 samples)
day6.part2: ~ (2504 ns 3655335 samples)
day7.part1: ~ (14 ms 708 samples)
day7.part2: ~ (14 ms 707 samples)
day8.part1: ~ (3084 μs 3242 samples)
day8.part2: ~ (23 ms 426 samples)
day9.part1: ~ (8535 μs 1172 samples)
day9.part2: ~ (8524 μs 1174 samples)
day10.part1: ~ (9845 μs 1016 samples)
day10.part2: ~ (35 ms 287 samples)
day11.part1: ~ (28 ms 360 samples)
day11.part2: ~ (31 ms 321 samples)
day12.part1: ~ (52 ms 193 samples)
day12.part2: ~ (779 ms 13 samples)
```
