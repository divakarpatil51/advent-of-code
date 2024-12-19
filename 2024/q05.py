from collections import defaultdict
import aocd


def part1(data: str) -> int:
    page_ordering_rules, update_page_numbers = data.split("\n\n")
    middle_pages_sum = 0

    rules: dict[int, set[int]] = defaultdict(set)
    for rule in page_ordering_rules.split("\n"):
        key, value = rule.split("|")
        rules[int(value)].add(int(key))

    for row in update_page_numbers.split("\n"):
        row = list(map(int, row.split(",")))
        for idx, page_number in enumerate(row):
            if page_number in rules and rules[page_number].intersection(set(row[idx:])):
                break
        else:
            middle_pages_sum += row[len(row) // 2]

    return middle_pages_sum


def order_pages(rules: dict[int, set[int]], row: list[int]) -> list[int]:
    for idx, page_number in enumerate(row):
        if intersection := rules[page_number].intersection(set(row[idx:])):
            last_idx = row.index(list(intersection)[-1])
            row[idx], row[last_idx] = row[last_idx], row[idx]
            return order_pages(rules, row[0:idx]) + order_pages(rules, row[idx:])

    return row


def part2(data: str) -> int:
    page_ordering_rules, update_page_numbers = data.split("\n\n")
    middle_page_numbers: list[int] = []

    rules: dict[int, set[int]] = defaultdict(set)
    for rule in page_ordering_rules.split("\n"):
        key, value = rule.split("|")
        rules[int(value)].add(int(key))

    for row in update_page_numbers.split("\n"):
        row = list(map(int, row.split(",")))
        for idx, page_number in enumerate(row):
            if page_number in rules and rules[page_number].intersection(set(row[idx:])):
                ordered_page = order_pages(rules, row)
                middle_page_numbers.append(ordered_page[len(ordered_page) // 2])
                break

    return sum(middle_page_numbers)


data = aocd.get_data(day=5, year=2024)
# data = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13
#
# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

assert part1(data) == 3608
assert part2(data) == 4922
print(f"Part 1 output: {part1(data)}")  # --> 3608
print(f"Part 2 output: {part2(data)}")  # --> 4922
