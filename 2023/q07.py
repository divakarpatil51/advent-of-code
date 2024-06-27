from collections import Counter
import re
from functools import cmp_to_key
import os


def is_five_of_a_kind(_char_dict: dict):
    # Five of a kind, where all five cards have the same label: AAAAA
    return len(_char_dict) == 1


def is_four_of_a_kind(_char_dict: dict):
    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    return len(_char_dict) == 2 and sorted(_char_dict.values()) == [1, 4]


def is_full_house(_char_dict: dict):
    # Full house, where three cards have the same label,
    # and the remaining two cards share a different label: 23332
    return len(_char_dict) == 2 and sorted(_char_dict.values()) == [2, 3]


def is_three_of_a_kind(_char_dict: dict):
    # Three of a kind, where three cards have the same label,
    # and the remaining two cards are each different from any other card in the hand: TTT98
    return len(_char_dict) == 3 and sorted(_char_dict.values()) == [1, 1, 3]


def is_two_pair(_char_dict: dict):
    # Two pair, where two cards share one label,
    # two other cards share a second label, and the remaining card has a third label: 23432
    return len(_char_dict) == 3 and sorted(_char_dict.values()) == [1, 2, 2]


def is_one_pair(_char_dict: dict):
    # One pair, where two cards share one label,
    # and the other three cards have a different label from the pair and each other: A23A4
    return len(_char_dict) == 4


def is_high_card(_char_dict: dict):
    # High card, where all cards' labels are distinct: 23456
    return len(_char_dict) == 5


def part_1(data: str):
    strength = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    def comparator(key1, key2):
        hand1, _, _type1 = key1
        hand2, _, _type2 = key2
        if _type1 > _type2:
            return 1
        elif _type1 < _type2:
            return -1
        if hand1 == hand2:
            return 0
        for _char1, _char2 in zip(hand1, hand2):
            if strength.index(_char1) > strength.index(_char2):
                return 1
            elif strength.index(_char1) < strength.index(_char2):
                return -1

        return -1

    sorted_by_type = []
    for row in re.findall(r"\w+ \w+", data):
        hand, bid = row.split()
        count = Counter(hand)
        if is_five_of_a_kind(count):
            sorted_by_type.append((hand, bid, 7))

        if is_four_of_a_kind(count):
            sorted_by_type.append((hand, bid, 6))
        if is_full_house(count):
            sorted_by_type.append((hand, bid, 5))
        if is_three_of_a_kind(count):
            sorted_by_type.append((hand, bid, 4))
        if is_two_pair(count):
            sorted_by_type.append((hand, bid, 3))
        if is_one_pair(count):
            sorted_by_type.append((hand, bid, 2))
        if is_high_card(count):
            sorted_by_type.append((hand, bid, 1))

    total_winnings = 0
    for idx, _hand in enumerate(
        sorted(sorted_by_type, key=cmp_to_key(comparator)), start=1
    ):
        total_winnings += idx * int(_hand[1])

    return total_winnings


def part_2(data: str):
    _strength = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

    def comparator_1(key1, key2):
        hand1, _, _type1 = key1
        hand2, _, _type2 = key2
        if _type1 > _type2:
            return 1
        elif _type1 < _type2:
            return -1
        if hand1 == hand2:
            return 0
        for _char1, _char2 in zip(hand1, hand2):
            if _strength.index(_char1) > _strength.index(_char2):
                return 1
            elif _strength.index(_char1) < _strength.index(_char2):
                return -1

        return -1

    def get_type(_char_dict: Counter):
        joker_count = _char_dict.get("J", 0)
        del _char_dict["J"]
        counts = sorted(list(_char_dict.values()), reverse=True) or [0]
        counts[0] += joker_count
        # Five of a kind, where all five cards have the same label: AAAAA
        if counts[0] == 5:
            return 7

        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        if counts[0] == 4:
            return 6

        # Full house, where three cards have the same label,
        # and the remaining two cards share a different label: 23332
        if (counts[0], counts[1]) == (3, 2):
            return 5

        # Three of a kind, where three cards have the same label,
        # and the remaining two cards are each different from any other card in the hand: TTT98
        if counts[0] == 3:
            return 4

        # Two pair, where two cards share one label,
        # two other cards share a second label, and the remaining card has a third label: 23432
        if (counts[0], counts[1], counts[2]) == (2, 2, 1):
            return 3

        # One pair, where two cards share one label,
        # and the other three cards have a different label from the pair and each other: A23A4
        if counts[0] == 2:
            return 2

        # High card, where all cards' labels are distinct: 23456
        return 1

    sorted_by_type = []
    for row in re.findall(r"\w+ \w+", data):
        hand, bid = row.split()
        count = Counter(hand)
        sorted_by_type.append((hand, bid, get_type(count)))

    total_winnings = 0
    for idx, _hand in enumerate(
        sorted(sorted_by_type, key=cmp_to_key(comparator_1)), start=1
    ):
        total_winnings += idx * int(_hand[1])

    return total_winnings


data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
with open(os.path.join(os.getcwd(), "2023/inputs/7.txt"), "r") as f:
    data = f.read().strip()
    print(f"Part one output: {part_1(data)}")
    print(f"Part two output: {part_2(data)}")
