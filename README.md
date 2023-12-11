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
imported: 11 solution(s) in 5133 μs
running: all with benchmark
day1.part1: ~ (795 μs 2516 samples)
day1.part2: ~ (4946 μs 405 samples)
day2.part1: ~ (419 μs 4766 samples)
day2.part2: ~ (691 μs 2895 samples)
day3.part1: ~ (3588 μs 558 samples)
day3.part2: ~ (3152 μs 635 samples)
day4.part1: ~ (1471 μs 1360 samples)
day4.part2: ~ (1651 μs 1211 samples)
day5.part1: ~ (287 μs 6958 samples)
day5.part2: ~ (4247 μs 471 samples)
day6.part1: ~ (21 μs 93344 samples)
day6.part2: ~ (2465 ns 747381 samples)
day7.part1: ~ (14 ms 146 samples)
day7.part2: ~ (14 ms 145 samples)
day8.part1: ~ (3080 μs 650 samples)
day8.part2: ~ (23 ms 88 samples)
day9.part1: ~ (8441 μs 237 samples)
day9.part2: ~ (8560 μs 234 samples)
day10.part1: ~ (9695 μs 207 samples)
day10.part2: ~ (34 ms 59 samples)
day11.part1: ~ (26 ms 77 samples)
day11.part2: ~ (30 ms 67 samples)
total: 192 ms
```
