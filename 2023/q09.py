import os


# Recursively subtract array
def part_1(data: str):
    def subtract_elements(arr: list, curr_total: int):
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


def part_2(data: str):
    def subtract_elements(arr: list, total_arr: list[int]):
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


data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

with open(os.path.join(os.getcwd(), "2023/inputs/9.txt"), "r") as f:
    data = f.read().strip()
    print(f"Part one output: {part_1(data)}")
    print(f"Part two output: {part_2(data)}")
