import os


from pathlib import Path


def read_input(year: str, day: str) -> str:
    """Read input data for Advent of Code problems."""
    env = os.getenv("AOC_ENV", "real")
    input_path = Path.cwd() / "inputs" / year / env / f"{day}.txt"
    return input_path.read_text().strip()


import re


def part_1(data: str):
    alamanac_data = data.split("\n\n")
    seeds = re.findall(r"\d+", alamanac_data.pop(0))

    nearest_loc = float("inf")
    for seed in map(int, seeds):
        curr_source = seed
        for line in alamanac_data:
            src_dest_map: list[str] = re.findall(r"\d+ \d+ \d+", line)
            for curr in src_dest_map:
                dest, source, _range = map(int, curr.split())
                if curr_source in range(source, source + _range):
                    curr_source = curr_source + dest - source
                    break
        nearest_loc = min(nearest_loc, curr_source)
    return nearest_loc


def part_2(puzzle_input: str):
    segments: list[str] = puzzle_input.split("\n\n")
    intervals: list[tuple[int, int, int]] = []

    seeds: list[str] = re.findall(r"(\d+) (\d+)", segments[0])
    for seed in seeds:
        src, _range = map(int, seed)
        intervals.append((src, src + _range, 1))

    min_location = float("inf")
    while intervals:
        src_start, src_end, level = intervals.pop()
        if level == 8:
            min_location = min(src_start, min_location)
            continue
        conversions: list[str] = re.findall(r"(\d+) (\d+) (\d+)", segments[level])
        for conversion in conversions:
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


data = read_input("2023", "5")
print(f"Part one output: {part_1(data)}")
print(f"Part two output: {part_2(data)}")
