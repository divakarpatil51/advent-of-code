import re
from collections import defaultdict


import os


def part_1(data: str):
    count = 0
    for line in data.strip().split("\n"):
        groups = re.split(r"Card .*: (.*) \| (.*)", line)
        winning_numbers = set(groups[1].split())
        our_numbers = set(groups[2].split())
        intersection = our_numbers.intersection(winning_numbers)
        if intersection:
            count += 2 ** (len(intersection) - 1)

    return count


def part_2(data: str):
    count = 0
    card_count = defaultdict(int)
    for idx, line in enumerate(data.strip().split("\n"), start=1):
        groups = re.split(r"Card .*: (.*) \| (.*)", line)
        winning_numbers = set(groups[1].split())
        our_numbers = set(groups[2].split())
        cards_won = len(our_numbers.intersection(winning_numbers))
        card_count[idx] += 1
        for card in range(1, cards_won + 1):
            next_card = idx + card
            card_count[next_card] += card_count.get(idx)
    return sum(card_count.values())


# data = aocd.get_data(day=4, year=2023)
data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11 """

with open(os.path.join(os.getcwd(), "2023/inputs/4.txt"), "r") as f:
    data = f.read().strip()
    print(f"Part one output: {part_1(data)}")
    print(f"Part two output: {part_2(data)}")
