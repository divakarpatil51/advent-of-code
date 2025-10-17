import dataclasses
import os
import re
from pathlib import Path


def read_input(year: str, day: str) -> str:
    """Read input data for Advent of Code problems."""
    env = os.getenv("AOC_ENV", "real")
    input_path = Path.cwd() / "inputs" / year / env / f"{day}.txt"
    return input_path.read_text().strip()


@dataclasses.dataclass
class Draw:
    r: int
    g: int
    b: int


@dataclasses.dataclass
class Game:
    idx: int
    draws: list[Draw]


def parse_line(line: str) -> Game:
    _set = re.match(r"Game (\d+): (.*)", line, re.IGNORECASE)
    assert _set

    idx = int(_set.group(1))
    draws = _set.group(2).split("; ")
    parsed_draws: list[Draw] = []
    for draw in draws:
        red_count, green_count, blue_count = 0, 0, 0
        green = re.search(r"(\d+) green", draw, re.IGNORECASE)
        if green:
            green_count = int(green.group(1))

        red = re.search(r"(\d+) red", draw, re.IGNORECASE)
        if red:
            red_count = int(red.group(1))

        blue = re.search(r"(\d+) blue", draw, re.IGNORECASE)
        if blue:
            blue_count = int(blue.group(1))

        parsed_draws.append(Draw(r=red_count, g=green_count, b=blue_count))
    return Game(idx=idx, draws=parsed_draws)


def part_1(data: str) -> int:
    total_count = 0
    for line in data.splitlines():
        game: Game = parse_line(line)
        for draw in game.draws:
            if draw.r > 12 or draw.g > 13 or draw.b > 14:
                break
        else:
            total_count += game.idx
    return total_count


def part_2(data: str) -> int:
    total_count = 0
    for line in data.splitlines():
        game: Game = parse_line(line)
        max_red = max(game.draws, key=lambda draw: draw.r)
        max_green = max(game.draws, key=lambda draw: draw.g)
        max_blue = max(game.draws, key=lambda draw: draw.b)
        total_count += max_red.r * max_green.g * max_blue.b
    return total_count


data = read_input("2023", "2")
print(f"Part one output: {part_1(data)}")
print(f"Part two output: {part_2(data)}")
