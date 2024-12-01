from pathlib import Path
from collections import Counter
import heapq


def part_1(data: str) -> int:
    left_list: list[int] = []
    right_list: list[int] = []
    for line in data.split("\n"):
        left, right = line.split("  ")
        heapq.heappush(left_list, int(left))
        heapq.heappush(right_list, int(right))

    count = 0
    for _ in range(len(left_list)):
        count += abs(heapq.heappop(left_list) - heapq.heappop(right_list))
    return count


def part_2(data: str) -> int:
    left_list: list[int] = []
    right_list: list[int] = []
    for line in data.split("\n"):
        left, right = line.split("  ")
        left_list.append(int(left))
        right_list.append(int(right))

    counter = Counter(right_list)
    count = 0
    for ele in left_list:
        count += counter[ele] * ele

    return count


data = Path(Path.cwd() / "2024/inputs/1.txt").read_text().strip()
print(f"Part one output: {part_1(data)}")
print(f"Part two output: {part_2(data)}")
