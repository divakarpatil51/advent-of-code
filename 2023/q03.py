import math
import re
from collections.abc import Iterable
from pathlib import Path


def is_symbol(_char: str):
    return _char != "." and not _char.isdigit()


def get_numbers(data: list[str]):
    for _, line in enumerate(data):
        for d in re.finditer(r"(\d)+", line):
            start_idx = d.start(0)
            end_idx = d.end(0) - 1
            yield start_idx, end_idx, int(d.group(0))


def part_1(data: str):
    count = 0
    _data = data.splitlines()
    symbol_adjacent_positions: set[tuple[int, int]] = set()
    for i, line in enumerate(_data):
        for m in re.finditer(r"[^.\d]", line):
            j = m.start()
            symbol_adjacent_positions |= {
                (r, c) for r in range(i - 1, i + 2) for c in range(j - 1, j + 2)
            }

    for i, line in enumerate(_data):
        for match in re.finditer(r"\d+", line):
            if any((i, j) in symbol_adjacent_positions for j in range(*match.span())):
                count += int(match.group())

    return count


def _is_adjacent(symbol_idx: int, num_idx: Iterable[int]):
    return (
        symbol_idx in num_idx or symbol_idx - 1 in num_idx or symbol_idx + 1 in num_idx
    )


def part_2(data: str):
    count = 0
    _data = data.splitlines()
    for idx, line in enumerate(_data):
        for sym_idx, _char in enumerate(line):
            if is_symbol(_char):
                start_idx = max(0, idx - 1)
                end_idx = min(idx + 1, len(_data) - 1)
                # This is inefficient as we are fetching same lines multiple times
                num_data = get_numbers(_data[start_idx : end_idx + 1])
                adjacent_count = 0
                nums: list[int] = []
                for _num in num_data:
                    num_s_idx, num_e_idx, curr_num = _num
                    if _is_adjacent(sym_idx, range(num_s_idx, num_e_idx + 1)):
                        adjacent_count += 1
                        nums.append(curr_num)
                if adjacent_count == 2:
                    count += math.prod(nums)

    return count


data = Path(Path.cwd() / "2023/inputs/3.txt").read_text().strip()
print(f"Part one output: {part_1(data)}")
print(f"Part two output: {part_2(data)}")
