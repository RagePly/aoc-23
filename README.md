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
imported: 13 solution(s) in 2208 μs
running: all with benchmark
day1.part1: ~ (789 μs 12664 samples)
day1.part2: ~ (4926 μs 2031 samples)
day2.part1: ~ (397 μs 25181 samples)
day2.part2: ~ (677 μs 14759 samples)
day3.part1: ~ (3610 μs 2770 samples)
day3.part2: ~ (3195 μs 3130 samples)
day4.part1: ~ (1458 μs 6856 samples)
day4.part2: ~ (1639 μs 6100 samples)
day5.part1: ~ (285 μs 35085 samples)
day5.part2: ~ (4220 μs 2370 samples)
day6.part1: ~ (21 μs 470028 samples)
day6.part2: ~ (2422 ns 3779234 samples)
day7.part1: ~ (14 ms 728 samples)
day7.part2: ~ (14 ms 724 samples)
day8.part1: ~ (3089 μs 3238 samples)
day8.part2: ~ (23 ms 436 samples)
day9.part1: ~ (8289 μs 1207 samples)
day9.part2: ~ (8265 μs 1210 samples)
day10.part1: ~ (9580 μs 1044 samples)
day10.part2: ~ (34 ms 294 samples)
day11.part1: ~ (26 ms 384 samples)
day11.part2: ~ (30 ms 335 samples)
day12.part1: ~ (52 ms 195 samples)
day12.part2: ~ (782 ms 13 samples)
day13.part1: ~ (3367 μs 2971 samples)
day13.part2: ~ (4947 μs 2022 samples)
total: 1033 ms
```
