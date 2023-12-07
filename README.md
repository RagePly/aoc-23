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
imported: 7 solution(s) in 5429 μs
running: all with benchmark
day1.part1: ~ (809 μs 2473 samples)
day1.part2: ~ (4916 μs 407 samples)
day2.part1: ~ (417 μs 4791 samples)
day2.part2: ~ (691 μs 2893 samples)
day3.part1: ~ (3638 μs 550 samples)
day3.part2: ~ (3162 μs 633 samples)
day4.part1: ~ (1458 μs 1372 samples)
day4.part2: ~ (1652 μs 1211 samples)
day5.part1: ~ (283 μs 7061 samples)
day5.part2: ~ (4185 μs 478 samples)
day6.part1: ~ (22 μs 90435 samples)
day6.part2: ~ (2473 ns 742804 samples)
day7.part1: ~ (14 ms 143 samples)
day7.part2: ~ (14 ms 144 samples)
total: 49 ms
```
