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
imported: 4 solution(s) in 3097 μs
running: all with benchmark
day1.part1: ~ (769 μs 2602 samples)
day1.part2: ~ (4961 μs 404 samples)
day2.part1: ~ (425 μs 4700 samples)
day2.part2: ~ (727 μs 2751 samples)
day3.part1: ~ (3592 μs 557 samples)
day3.part2: ~ (3219 μs 622 samples)
day4.part1: ~ (1465 μs 1366 samples)
day4.part2: ~ (1680 μs 1191 samples)
total: 17 ms
```
