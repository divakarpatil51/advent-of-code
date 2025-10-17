import os


from pathlib import Path


def read_input(year: str, day: str) -> str:
    """Read input data for Advent of Code problems."""
    env = os.getenv("AOC_ENV", "real")
    input_path = Path.cwd() / "inputs" / year / env / f"{day}.txt"
    return input_path.read_text().strip()




# Recursively subtract array
def part_1(data: str) -> int:
    def subtract_elements(arr: list[int], curr_total: int) -> int:
        if all(ele == 0 for ele in arr):
            return curr_total
        new_arr = [ele[0] - ele[1] for ele in zip(arr[1:], arr[:-1])]
        return subtract_elements(new_arr, curr_total + new_arr[-1])

    total = 0
    for row in data.split("\n"):
        _arr = list(map(int, row.split()))
        print(_arr)
        total += subtract_elements(_arr, _arr[-1])
    return total


def part_2(data: str) -> int:
    def subtract_elements(arr: list[int], total_arr: list[int]) -> list[int]:
        if all(ele == 0 for ele in arr):
            return total_arr
        new_arr = [ele[0] - ele[1] for ele in zip(arr[1:], arr[:-1])]
        total_arr.append(new_arr[0])
        return subtract_elements(new_arr, total_arr)

    total = 0
    for row in data.split("\n"):
        _arr = list(map(int, row.split()))
        total_arr = subtract_elements(_arr, [_arr[0]])
        for idx, ele in enumerate(total_arr):
            total += ele if idx % 2 == 0 else -ele
    return total


data = read_input("2023", "9")
print(f"Part one output: {part_1(data)}")
print(f"Part two output: {part_2(data)}")
