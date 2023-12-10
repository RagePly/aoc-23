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
imported: 10 solution(s) in 1793 μs
running: all with benchmark
day1.part1: ~ (779 μs 2566 samples)
day1.part2: ~ (4936 μs 406 samples)
day2.part1: ~ (414 μs 4832 samples)
day2.part2: ~ (675 μs 2962 samples)
day3.part1: ~ (3797 μs 527 samples)
day3.part2: ~ (3323 μs 602 samples)
day4.part1: ~ (1506 μs 1328 samples)
day4.part2: ~ (1640 μs 1219 samples)
day5.part1: ~ (287 μs 6970 samples)
day5.part2: ~ (4281 μs 468 samples)
day6.part1: ~ (25 μs 79824 samples)
day6.part2: ~ (2511 ns 730984 samples)
day7.part1: ~ (15 ms 134 samples)
day7.part2: ~ (15 ms 135 samples)
day8.part1: ~ (4183 μs 479 samples)
day8.part2: ~ (34 ms 59 samples)
day9.part1: ~ (12 ms 167 samples)
day9.part2: ~ (13 ms 156 samples)
day10.part1: ~ (11 ms 187 samples)
day10.part2: ~ (50 ms 40 samples)
total: 176 ms
```
