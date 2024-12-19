import aocd


directions = [
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 0), (1, 1), (2, 2), (3, 3)),
    ((0, 0), (-1, 1), (-2, 2), (-3, 3)),
    ((0, 0), (1, -1), (2, -2), (3, -3)),
    ((0, 0), (-1, -1), (-2, -2), (-3, -3)),
    ((0, 0), (-1, 0), (-2, 0), (-3, 0)),
    ((0, 0), (0, -1), (0, -2), (0, -3)),
]


def part1(data: str) -> int:
    word = "XMAS"
    count = 0
    ip: list[list[str]] = []
    for line in data.split("\n"):
        ip.append(list(line))

    for i in range(len(ip)):
        for j in range(len(ip[i])):
            for direction in directions:
                for k in range(4):
                    new_i = i + direction[k][0]
                    new_j = j + direction[k][1]
                    if (new_i < 0 or new_j < 0 or new_i >= len(ip) or new_j >= len(ip[0])) or ip[
                        new_i
                    ][new_j] != word[k]:
                        break
                else:
                    count += 1
    return count


def part2(data: str) -> int:
    count = 0
    ip: list[list[str]] = []
    for line in data.split("\n"):
        ip.append(list(line))
    for i in range(len(ip)):
        for j in range(len(ip[i])):
            try:
                diagonal1 = ip[i - 1][j - 1] + ip[i][j] + ip[i + 1][j + 1]
                diagonal2 = ip[i - 1][j + 1] + ip[i][j] + ip[i + 1][j - 1]

                if diagonal1 in ["MAS", "SAM"] and diagonal2 in ["MAS", "SAM"]:
                    count += 1
            except IndexError:
                pass

    return count


data: str = aocd.get_data(day=4, year=2024)


# data = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX"""

print(f"Part 1 output: {part1(data)}")  # 2447

print(f"Part 2 output: {part2(data)}")  # 1868
