import re
import os


def part_1(data: str):
    alamanac_data = data.split("\n\n")
    seeds = re.findall(r"\d+", alamanac_data.pop(0))

    nearest_loc = float("inf")
    for seed in map(int, seeds):
        curr_source = seed
        for line in alamanac_data:
            src_dest_map = re.findall(r"\d+ \d+ \d+", line)
            for curr in src_dest_map:
                dest, source, _range = map(int, curr.split())
                if curr_source in range(source, source + _range):
                    curr_source = curr_source + dest - source
                    break
        nearest_loc = min(nearest_loc, curr_source)
    return nearest_loc


def part_2(puzzle_input: str):
    segments = puzzle_input.split("\n\n")
    intervals = []

    for seed in re.findall(r"(\d+) (\d+)", segments[0]):
        src, _range = map(int, seed)
        intervals.append((src, src + _range, 1))

    min_location = float("inf")
    while intervals:
        src_start, src_end, level = intervals.pop()
        if level == 8:
            min_location = min(src_start, min_location)
            continue

        for conversion in re.findall(r"(\d+) (\d+) (\d+)", segments[level]):
            dest, new_src_start, _range = map(int, conversion)
            new_src_end = new_src_start + _range
            diff = dest - new_src_start

            if src_end <= new_src_start or new_src_end <= src_start:  # no overlap
                continue
            if src_start < new_src_start:  # split original interval at y1
                intervals.append((src_start, new_src_start, level))
                src_start = new_src_start
            if new_src_end < src_end:  # split original interval at y2
                intervals.append((new_src_end, src_end, level))
                src_end = new_src_end
            # perfect overlap -> make conversion and let pass to next nevel
            intervals.append((src_start + diff, src_end + diff, level + 1))
            break

        else:
            intervals.append((src_start, src_end, level + 1))
    return min_location


data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


with open(os.path.join(os.getcwd(), "2023/inputs/5.txt"), "r") as f:
    data = f.read().strip()
    print(f"Part one output: {part_1(data)}")
    print(f"Part two output: {part_2(data)}")
