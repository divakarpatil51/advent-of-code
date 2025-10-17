import os


from pathlib import Path


def read_input(year: str, day: str) -> str:
    """Read input data for Advent of Code problems."""
    env = os.getenv("AOC_ENV", "real")
    input_path = Path.cwd() / "inputs" / year / env / f"{day}.txt"
    return input_path.read_text().strip()


import re


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


data = read_input("2023", "6")
print(f"Part one output: {part_1(data)}")
print(f"Part two output: {part_2(data)}")
