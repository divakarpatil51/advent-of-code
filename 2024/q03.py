import aocd
import re


def part1(data: str) -> int:
    count = 0
    for num1, num2 in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data):
        count += int(num1) * int(num2)
    return count


def part2(data: str) -> int:
    count = 0
    for dont in re.finditer(r"don't\(\).*?((do\(\))|$)", data.replace("\n", "")):
        for num1, num2 in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", dont.group()):
            count += int(num1) * int(num2)

    data = re.sub(r"don't\(\).*?((do\(\))|$)", "", data.replace("\n", ""))
    return count


data = aocd.get_data(day=3, year=2024)
print(f"Part 1 output: {part1(data)}")
print(f"Part 2 output: {part2(data)}")
