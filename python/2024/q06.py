import attrs
import aocd


@attrs.frozen
class Point:
    row: int
    col: int

    def __add__(self, other: "Point") -> "Point":
        return Point(self.row + other.row, self.col + other.col)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.row == other.row and self.col == other.col

    def __hash__(self) -> int:
        return hash((self.row, self.col))


direction = {
    "N": ("E", Point(-1, 0)),
    "E": ("S", Point(0, 1)),
    "S": ("W", Point(1, 0)),
    "W": ("N", Point(0, -1)),
}


def is_out_of_bounds(grid: list[list[str]], point: Point) -> bool:
    return not (0 <= point.row < len(grid) and 0 <= point.col < len(grid[0]))


def read_grid_and_guard_pos(data: str) -> tuple[list[list[str]], Point]:
    grid: list[list[str]] = []
    guard_pos: Point | None = None
    for idx, line in enumerate(data.split("\n")):
        grid.append(list(line))
        if "^" in line:
            guard_pos = Point(idx, line.index("^"))

    assert guard_pos is not None
    return grid, guard_pos


def part1(data: str) -> int:
    grid, guard_pos = read_grid_and_guard_pos(data)

    curr_dir = "N"
    visited: set[tuple[Point, str]] = {(guard_pos, curr_dir)}
    while True:
        next_pos = guard_pos + direction[curr_dir][1]

        if is_out_of_bounds(grid, next_pos):
            break

        if grid[next_pos.row][next_pos.col] == "#":
            curr_dir = direction[curr_dir][0]
            continue

        guard_pos = next_pos
        if (guard_pos, curr_dir) in visited:
            break

        visited.add((guard_pos, curr_dir))

    return len({visited_point[0] for visited_point in visited})


def forms_a_loop(
    grid: list[list[str]],
    guard_pos: Point,
    curr_dir: str,
) -> tuple[set[tuple[Point, str]], bool]:
    visited: set[tuple[Point, str]] = {(guard_pos, curr_dir)}
    while True:
        next_pos = guard_pos + direction[curr_dir][1]

        if is_out_of_bounds(grid, next_pos):
            return visited, False

        if grid[next_pos.row][next_pos.col] == "#":
            curr_dir = direction[curr_dir][0]
            continue

        guard_pos = next_pos
        if (guard_pos, curr_dir) in visited:
            return visited, True
        visited.add((guard_pos, curr_dir))


def part2(data: str) -> int:
    grid, guard_pos = read_grid_and_guard_pos(data)
    print(" ", list(map(lambda ele: str(ele), list(range(len(grid[0]))))))
    for idx, row in enumerate(grid):
        print(idx, row)

    visited, _ = forms_a_loop(grid, guard_pos, "N")
    visited_points = {visited_point[0] for visited_point in visited}
    visited_points.remove(guard_pos)
    count = 0
    for point in visited_points:
        grid[point.row][point.col] = "#"
        _, in_loop = forms_a_loop(grid, guard_pos, "N")
        if in_loop:
            count += 1
        grid[point.row][point.col] = "."
    return count


data = aocd.get_data(day=6, year=2024)

print(f"Part 1 output: {part1(data)}")
print(f"Part 2 output: {part2(data)}")
