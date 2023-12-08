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
imported: 8 solution(s) in 4652 μs
running: all with benchmark
day1.part1: ~ (795 μs 2516 samples)
day1.part2: ~ (4920 μs 407 samples)
day2.part1: ~ (423 μs 4722 samples)
day2.part2: ~ (703 μs 2843 samples)
day3.part1: ~ (3656 μs 547 samples)
day3.part2: ~ (3241 μs 618 samples)
day4.part1: ~ (1457 μs 1373 samples)
day4.part2: ~ (1646 μs 1215 samples)
day5.part1: ~ (287 μs 6969 samples)
day5.part2: ~ (4258 μs 470 samples)
day6.part1: ~ (21 μs 93652 samples)
day6.part2: ~ (2551 ns 725373 samples)
day7.part1: ~ (14 ms 145 samples)
day7.part2: ~ (14 ms 145 samples)
day8.part1: ~ (3126 μs 640 samples)
day8.part2: ~ (24 ms 85 samples)
total: 76 ms
```
