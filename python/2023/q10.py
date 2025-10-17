import os


from collections import deque
from pathlib import Path


def read_input(year: str, day: str) -> str:
    """Read input data for Advent of Code problems."""
    env = os.getenv("AOC_ENV", "real")
    input_path = Path.cwd() / "inputs" / year / env / f"{day}.txt"
    return input_path.read_text().strip()




def part1(data: str):
    grid = []
    stack: deque[tuple[int, int]] = deque()
    seen: set[tuple[int, int]] = set()
    grid = data.split()
    for row, line in enumerate(grid):
        for col, element in enumerate(line):
            if element == "S":
                stack.append((row, col))
                seen.add((row, col))
                break

    row_count = len(grid)
    col_count = len(grid[0])
    while stack:
        row, col = stack.popleft()
        if row < 0 or col < 0 or row > row_count or col > col_count:
            continue
        cell = grid[row][col]
        # Traveling down
        if (row + 1, col) not in seen and cell in "7F|S" and grid[row + 1][col] in "|JL":
            curr = row + 1, col
            stack.append(curr)
            seen.add(curr)

        # Traveling up
        if (row - 1, col) not in seen and cell in "J|SL" and grid[row - 1][col] in "|7F":
            curr = row - 1, col
            stack.append(curr)
            seen.add(curr)

        # Traveling right
        if (row, col + 1) not in seen and cell in "-FLS" and grid[row][col + 1] in "-7J":
            curr = row, col + 1
            stack.append(curr)
            seen.add(curr)

        # Traveling left
        if (row, col - 1) not in seen and cell in "-7JS" and grid[row][col - 1] in "-FL":
            curr = row, col - 1
            stack.append(curr)
            seen.add(curr)

    # Since we are traveling in 2 directions for src->dest, dividing our length of set by 2
    return len(seen) // 2


def part2(data: str):
    pass


data = read_input("2023", "10")
print(f"Part 1 output: {part1(data)}")
print(f"Part 2 output: {part2(data)}")
