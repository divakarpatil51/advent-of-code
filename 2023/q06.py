import re
import os


def part_1(data: str):
    time, distance = data.split("\n")
    distances = list(map(int, re.findall(r"\d+", distance)))
    num_of_ways = 1
    for idx, _time in enumerate(map(int, re.findall(r"\d+", time))):
        count = 0
        for ms in range(0, _time):
            time_taken = (_time - ms) * ms
            if time_taken > distances[idx]:
                count += 1
        num_of_ways *= count

    return num_of_ways


def part_2(data: str):
    time, distance = data.split("\n")
    total_time = int("".join(re.findall(r"\d+", time)))
    total_distance = int("".join(re.findall(r"\d+", distance)))
    num_of_ways = 0
    for ms in range(0, total_time):
        time_taken = (total_time - ms) * ms
        if time_taken > total_distance:
            num_of_ways += 1

    return num_of_ways


data = """
Time:      7  15   30
Distance:  9  40  200
"""

with open(os.path.join(os.getcwd(), "2023/inputs/6.txt"), "r") as f:
    data = f.read().strip()
    print(f"Part one output: {part_1(data)}")
    print(f"Part two output: {part_2(data)}")
