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
imported: 18 solution(s) in 21 ms
running: all with benchmark
day1.part1: ~ (767 μs 13037 samples)
day1.part2: ~ (5020 μs 1992 samples)
day2.part1: ~ (418 μs 23902 samples)
day2.part2: ~ (703 μs 14229 samples)
day3.part1: ~ (3735 μs 2678 samples)
day3.part2: ~ (3195 μs 3130 samples)
day4.part1: ~ (1510 μs 6621 samples)
day4.part2: ~ (1703 μs 5870 samples)
day5.part1: ~ (287 μs 34789 samples)
day5.part2: ~ (4298 μs 2327 samples)
day6.part1: ~ (22 μs 452271 samples)
day6.part2: ~ (2483 ns 3707537 samples)
day7.part1: ~ (14 ms 691 samples)
day7.part2: ~ (14 ms 692 samples)
day8.part1: ~ (3220 μs 3106 samples)
day8.part2: ~ (26 ms 392 samples)
day9.part1: ~ (8649 μs 1157 samples)
day9.part2: ~ (8671 μs 1154 samples)
day10.part1: ~ (10 ms 990 samples)
day10.part2: ~ (36 ms 282 samples)
day11.part1: ~ (27 ms 370 samples)
day11.part2: ~ (34 ms 298 samples)
day12.part1: ~ (52 ms 193 samples)
day12.part2: ~ (785 ms 13 samples)
day13.part1: ~ (3327 μs 3006 samples)
day13.part2: ~ (4938 μs 2025 samples)
day14.part1: ~ (4159 μs 2404 samples)
day14.part2: ~ (1905 ms 6 samples)
day15.part1: ~ (2263 μs 4419 samples)
day15.part2: ~ (4565 μs 2191 samples)
day16.part1: ~ (8239 μs 1214 samples)
day16.part2: ~ (1817 ms 6 samples)
day17.part1: ~ (1228 ms 9 samples)
day17.part2: ~ (4415 ms 3 samples)
day18.part1: ~ (223 ms 45 samples)
day18.part2: ~ (2637 ms 4 samples)
total: 13 s
```
