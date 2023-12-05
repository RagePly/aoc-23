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
imported: 5 solution(s) in 1084 μs
running: all with benchmark
day1.part1: ~ (766 μs 2610 samples)
day1.part2: ~ (4921 μs 407 samples)
day2.part1: ~ (416 μs 4800 samples)
day2.part2: ~ (693 μs 2884 samples)
day3.part1: ~ (3598 μs 556 samples)
day3.part2: ~ (3134 μs 639 samples)
day4.part1: ~ (1446 μs 1383 samples)
day4.part2: ~ (1632 μs 1225 samples)
day5.part1: ~ (282 μs 7072 samples)
day5.part2: ~ (4248 μs 471 samples)
total: 21 ms
```
