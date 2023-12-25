# AoC 2023 Solutions

Repo for 2023 AoC solutions.

## Score

My scores for each problem.

With the exception of day 1, 2, 3, 21 and 22, I started the problem at release and finished both parts on the same day. I did not have time to do part 2 of day 20 on the same day. I also waited to finish day 20 (part 2), 21 and 22 on the 25th.

I'm very happy about this year's results; I've managed to score a rank below 1000 on some days and finished all problems before the end of the 25th. Special shout out to [graphviz](https://pypi.org/project/graphviz/) for saving my a\*\* a good number of days.

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 25   00:24:04    482      0   09:22:01   4751      0
 24   01:27:38   2362      0   02:32:50   1132      0
 23   00:21:06    697      0   04:17:20   2748      0
 22       >24h  13530      0       >24h  12535      0
 21       >24h  19832      0       >24h  11447      0
 20   00:47:24    858      0       >24h  15383      0
 19   00:21:14    822      0   00:54:17    792      0
 18   00:25:44   1241      0   01:20:07   1634      0
 17   00:52:34   1325      0   01:02:12   1151      0
 16   00:21:48    804      0   00:32:10   1096      0
 15   00:07:19   2446      0   00:24:17   1451      0
 14   00:17:17   2717      0   01:00:59   2408      0
 13   00:32:16   2370      0   00:38:44   1508      0
 12   00:48:31   3469      0   03:15:47   3365      0
 11   00:17:36   1631      0   00:18:42    799      0
 10   00:19:59    561      0   01:54:29   2354      0
  9   00:10:41   1419      0   00:13:22   1186      0
  8   00:04:44    320      0   00:16:49    443      0
  7   00:28:53   2302      0   00:36:50   1441      0
  6   00:09:02   2189      0   00:32:05   7618      0
  5   00:17:58   1050      0   02:05:30   4573      0
  4   00:07:32   1865      0   00:16:45   1529      0
  3   05:36:14  26552      0   05:45:49  21029      0
  2   03:40:44  24646      0   03:43:44  22813      0
  1   05:07:04  44267      0   05:31:05  27563      0
```



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
imported: 25 solution(s) in 251 ms
running: all with benchmark
day1.part1: ~ (810 μs 12338 samples)
day1.part2: ~ (4932 μs 2028 samples)
day2.part1: ~ (418 μs 23888 samples)
day2.part2: ~ (695 μs 14373 samples)
day3.part1: ~ (3641 μs 2746 samples)
day3.part2: ~ (3142 μs 3183 samples)
day4.part1: ~ (1456 μs 6868 samples)
day4.part2: ~ (1644 μs 6080 samples)
day5.part1: ~ (286 μs 34885 samples)
day5.part2: ~ (4241 μs 2358 samples)
day6.part1: ~ (22 μs 454811 samples)
day6.part2: ~ (2465 ns 3708989 samples)
day7.part1: ~ (15 ms 688 samples)
day7.part2: ~ (15 ms 690 samples)
day8.part1: ~ (3089 μs 3238 samples)
day8.part2: ~ (24 ms 422 samples)
day9.part1: ~ (8552 μs 1170 samples)
day9.part2: ~ (8627 μs 1160 samples)
day10.part1: ~ (9798 μs 1021 samples)
day10.part2: ~ (35 ms 285 samples)
day11.part1: ~ (27 ms 364 samples)
day11.part2: ~ (31 ms 323 samples)
day12.part1: ~ (51 ms 195 samples)
day12.part2: ~ (786 ms 13 samples)
day13.part1: ~ (3400 μs 2941 samples)
day13.part2: ~ (5110 μs 1957 samples)
day14.part1: ~ (4157 μs 2406 samples)
day14.part2: ~ (1828 ms 6 samples)
day15.part1: ~ (2310 μs 4329 samples)
day15.part2: ~ (4358 μs 2295 samples)
day16.part1: ~ (11 ms 948 samples)
day16.part2: ~ (2234 ms 5 samples)
day17.part1: ~ (1279 ms 8 samples)
day17.part2: ~ (4669 ms 3 samples)
day18.part1: ~ (218 ms 46 samples)
day18.part2: ~ (3290 ms 4 samples)
day19.part1: ~ (1617 μs 6184 samples)
day19.part2: ~ (2883 μs 3469 samples)
day20.part1: ~ (21 ms 481 samples)
day20.part2: ~ (74 μs 134013 samples)
day21.part1: ~ (74 ms 136 samples)
day21.part2: ~ (16 s)
day22.part1: ~ (13 ms 748 samples)
day22.part2: ~ (709 ms 15 samples)
day23.part1: ~ (7353 ms 2 samples)
day23.part2: ~ (66 s)
day24.part1: ~ (54 ms 187 samples)
day24.part2: ~ (163 ms 62 samples)
day25.part1: ~ (6977 ms 2 samples)
day25.part2: ~ (0 s)
total: 112 s
```
