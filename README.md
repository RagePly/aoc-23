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
imported: 6 solution(s) in 1107 μs
running: all with benchmark
day1.part1: ~ (798 μs 2507 samples)
day1.part2: ~ (4849 μs 413 samples)
day2.part1: ~ (405 μs 4931 samples)
day2.part2: ~ (667 μs 2998 samples)
day3.part1: ~ (3699 μs 541 samples)
day3.part2: ~ (3194 μs 627 samples)
day4.part1: ~ (1439 μs 1390 samples)
day4.part2: ~ (1624 μs 1232 samples)
day5.part1: ~ (280 μs 7138 samples)
day5.part2: ~ (4149 μs 482 samples)
day6.part1: ~ (21 μs 94144 samples)
day6.part2: ~ (2451 ns 747905 samples)
total: 21 ms
```
