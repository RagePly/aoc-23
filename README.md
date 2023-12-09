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
imported: 9 solution(s) in 4219 μs
running: all with benchmark
day1.part1: ~ (799 μs 2504 samples)
day1.part2: ~ (5000 μs 400 samples)
day2.part1: ~ (413 μs 4840 samples)
day2.part2: ~ (672 μs 2977 samples)
day3.part1: ~ (3648 μs 549 samples)
day3.part2: ~ (3143 μs 637 samples)
day4.part1: ~ (1484 μs 1347 samples)
day4.part2: ~ (1755 μs 1139 samples)
day5.part1: ~ (292 μs 6833 samples)
day5.part2: ~ (4202 μs 476 samples)
day6.part1: ~ (21 μs 93598 samples)
day6.part2: ~ (2436 ns 755722 samples)
day7.part1: ~ (14 ms 145 samples)
day7.part2: ~ (14 ms 144 samples)
day8.part1: ~ (3130 μs 639 samples)
day8.part2: ~ (24 ms 85 samples)
day9.part1: ~ (8363 μs 240 samples)
day9.part2: ~ (8400 μs 239 samples)
total: 93 ms
```
