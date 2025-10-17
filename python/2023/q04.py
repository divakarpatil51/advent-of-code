import os
import re
from collections import defaultdict
from pathlib import Path


def read_input(year: str, day: str) -> str:
    """Read input data for Advent of Code problems."""
    env = os.getenv("AOC_ENV", "real")
    input_path = Path.cwd() / "inputs" / year / env / f"{day}.txt"
    return input_path.read_text().strip()


def part_1(data: str):
    count: int = 0
    for line in data.strip().split("\n"):
        groups = re.split(r"Card .*: (.*) \| (.*)", line)
        winning_numbers = set(groups[1].split())
        our_numbers = set(groups[2].split())
        intersection = our_numbers.intersection(winning_numbers)
        if intersection:
            count += 2 ** (len(intersection) - 1)

    return count


def part_2(data: str):
    card_count: dict[int, int] = defaultdict(int)
    for idx, line in enumerate(data.strip().split("\n"), start=1):
        groups = re.split(r"Card .*: (.*) \| (.*)", line)
        winning_numbers = set(groups[1].split())
        our_numbers = set(groups[2].split())
        cards_won = len(our_numbers.intersection(winning_numbers))
        card_count[idx] += 1
        for card in range(1, cards_won + 1):
            next_card = idx + card
            card_count[next_card] += card_count[idx]
    return sum(card_count.values())


data = read_input("2023", "4")
print(f"Part one output: {part_1(data)}")
print(f"Part two output: {part_2(data)}")
