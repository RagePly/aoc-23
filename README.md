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
imported: 14 solution(s) in 2351 μs
running: all with benchmark
day1.part1: ~ (807 μs 12390 samples)
day1.part2: ~ (4887 μs 2047 samples)
day2.part1: ~ (404 μs 24748 samples)
day2.part2: ~ (685 μs 14589 samples)
day3.part1: ~ (3656 μs 2735 samples)
day3.part2: ~ (3135 μs 3190 samples)
day4.part1: ~ (1457 μs 6862 samples)
day4.part2: ~ (1656 μs 6038 samples)
day5.part1: ~ (287 μs 34747 samples)
day5.part2: ~ (4231 μs 2364 samples)
day6.part1: ~ (22 μs 445570 samples)
day6.part2: ~ (2504 ns 3661554 samples)
day7.part1: ~ (14 ms 692 samples)
day7.part2: ~ (15 ms 689 samples)
day8.part1: ~ (3069 μs 3259 samples)
day8.part2: ~ (23 ms 427 samples)
day9.part1: ~ (8560 μs 1169 samples)
day9.part2: ~ (8499 μs 1177 samples)
day10.part1: ~ (10 ms 1000 samples)
day10.part2: ~ (35 ms 286 samples)
day11.part1: ~ (26 ms 383 samples)
day11.part2: ~ (29 ms 340 samples)
day12.part1: ~ (51 ms 196 samples)
day12.part2: ~ (772 ms 13 samples)
day13.part1: ~ (3265 μs 3063 samples)
day13.part2: ~ (4822 μs 2074 samples)
day14.part1: ~ (3917 μs 2553 samples)
day14.part2: ~ (1733 ms 6 samples)
total: 2763 ms
```
