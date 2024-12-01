from pathlib import Path


def part_1(data: str) -> int:
    calibration_value = 0
    for line in data.split("\n"):
        digits = ""
        for _char in line:
            if _char.isdigit():
                digits += _char
        calibration_value += int(digits[0] + digits[-1])
    return calibration_value


def part_2(data: str) -> int:
    words = (
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "zero",
    )

    calibration_value = 0
    for line in data.split("\n"):
        digits: list[str] = []
        for idx, _char in enumerate(line):
            if _char.isdigit():
                digits.append(_char)
            else:
                for num, word in enumerate(words, 1):
                    if line[idx : idx + len(word)].startswith(word):
                        digits.append(str(num))
                        break
        calibration_value += int(digits[0] + digits[-1])
    return calibration_value


data = Path(Path.cwd() / "2023/inputs/1.txt").read_text().strip()
print(f"Part one output: {part_1(data)}")
print(f"Part two output: {part_2(data)}")
