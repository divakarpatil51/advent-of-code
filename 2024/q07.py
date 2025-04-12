import aocd
from typing import Callable


def sum(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def test(
    first_num: int, remaining_num: list[int], operators: list[Callable[[int, int], int]]
) -> list[int]:
    if not remaining_num:
        return [first_num]
    output: list[int] = []
    for operator in operators:
        output.extend(test(operator(first_num, remaining_num[0]), remaining_num[1:], operators))
    return output


def part1(data: str) -> int:
    output = 0
    operators = [sum, mul]
    for line in data.split("\n"):
        test_value, numbers = line.split(": ")
        numbers = list(map(int, numbers.split(" ")))
        if int(test_value) in test(numbers[0], numbers[1:], operators):
            output += int(test_value)
    return output


def part2(data: str) -> int:
    output = 0
    operators = [sum, mul, concat]
    for line in data.split("\n"):
        test_value, numbers = line.split(": ")
        numbers = list(map(int, numbers.split(" ")))
        if int(test_value) in test(numbers[0], numbers[1:], operators):
            output += int(test_value)
    return output


data = aocd.get_data(day=7, year=2024)
# data = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

print(f"Part 1 output: {part1(data)}")
print(f"Part 2 output: {part2(data)}")
