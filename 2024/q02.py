from pathlib import Path


def part1(data: str) -> int:
    count = 0
    reports = [list(map(int, line.split(" "))) for line in data.split("\n")]
    for report in reports:
        increasing_or_decreasing = all(
            report[i] < report[i + 1] for i in range(len(report) - 1)
        ) or all(report[i] > report[i + 1] for i in range(len(report) - 1))

        all_within_tolerance = all(
            1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1)
        )

        if increasing_or_decreasing and all_within_tolerance:
            count += 1

    return count


def part2(data: str) -> int:
    count = 0
    reports = [list(map(int, line.split(" "))) for line in data.split("\n")]
    for report in reports:
        is_safe = False
        for i in range(len(report)):
            excluded_list = list(report[:i]) + list(report[i + 1 :])
            increasing_or_decreasing = all(
                excluded_list[j] < excluded_list[j + 1]
                for j in range(len(excluded_list) - 1)
            ) or all(
                excluded_list[j] > excluded_list[j + 1]
                for j in range(len(excluded_list) - 1)
            )

            all_within_tolerance = all(
                1 <= abs(excluded_list[j] - excluded_list[j + 1]) <= 3
                for j in range(len(excluded_list) - 1)
            )

            if increasing_or_decreasing and all_within_tolerance:
                is_safe = True
                break
        if is_safe:
            count += 1

    return count


data = Path(Path.cwd() / "2024/inputs/2.txt").read_text().strip()
print(f"Part 1 output: {part1(data)}")  # 218 --> answer
print(f"Part 2 output: {part2(data)}")  # 290
