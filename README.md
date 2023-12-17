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
imported: 17 solution(s) in 2800 μs
running: all with benchmark
day1.part1: ~ (763 μs 13103 samples)
day1.part2: ~ (5084 μs 1967 samples)
day2.part1: ~ (411 μs 24333 samples)
day2.part2: ~ (686 μs 14561 samples)
day3.part1: ~ (3683 μs 2715 samples)
day3.part2: ~ (3139 μs 3186 samples)
day4.part1: ~ (1530 μs 6535 samples)
day4.part2: ~ (1661 μs 6018 samples)
day5.part1: ~ (278 μs 35913 samples)
day5.part2: ~ (4199 μs 2382 samples)
day6.part1: ~ (22 μs 455560 samples)
day6.part2: ~ (2481 ns 3703128 samples)
day7.part1: ~ (14 ms 719 samples)
day7.part2: ~ (14 ms 707 samples)
day8.part1: ~ (3116 μs 3209 samples)
day8.part2: ~ (23 ms 429 samples)
day9.part1: ~ (9088 μs 1101 samples)
day9.part2: ~ (9138 μs 1095 samples)
day10.part1: ~ (9709 μs 1030 samples)
day10.part2: ~ (36 ms 276 samples)
day11.part1: ~ (28 ms 359 samples)
day11.part2: ~ (34 ms 298 samples)
day12.part1: ~ (53 ms 189 samples)
day12.part2: ~ (767 ms 14 samples)
day13.part1: ~ (3247 μs 3079 samples)
day13.part2: ~ (4890 μs 2045 samples)
day14.part1: ~ (3899 μs 2565 samples)
day14.part2: ~ (1728 ms 6 samples)
day15.part1: ~ (2214 μs 4516 samples)
day15.part2: ~ (4246 μs 2356 samples)
day16.part1: ~ (8007 μs 1249 samples)
day16.part2: ~ (1715 ms 6 samples)
day17.part1: ~ (1234 ms 9 samples)
day17.part2: ~ (4286 ms 3 samples)
total: 10 s
```
