from aocd import lines, submit
from itertools import pairwise
from collections import defaultdict


class Grid:
    def __init__(self, void):
        self.void = void
        self.grid = {}
        self.min_x = 500
        self.max_x = 500
        self.max_y = 0

    def add_rock(self, x, y):
        self.grid[(x, y)] = "#"
        if x < self.min_x:
            self.min_x = x
        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y

    def is_air(self, x, y):
        if not self.void and y == self.max_y + 2:
            return False

        return (x, y) not in self.grid

    def in_bounds(self, x, y):
        if self.void:
            return x >= self.min_x and x <= self.max_x and y <= self.max_y
        else:
            return True

    def flow_sand(self):
        # Start at 500,0, and flow down until we hit something
        x, y = 500, 0

        while self.in_bounds(x, y):
            if self.is_air(x, y + 1):
                y += 1
                continue
            # We hit something, so we need to check left and right
            if self.is_air(x - 1, y + 1):  # left and down
                x -= 1
                y += 1
                continue
            if self.is_air(x + 1, y + 1):  # right and down
                x += 1
                y += 1
                continue
            if x == 500 and y == 0:
                return True
            self.grid[(x, y)] = "o"
            return False

    def draw_line(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1

            for y in range(y1, y2 + 1):
                self.add_rock(x1, y)
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                self.add_rock(x, y1)

    def draw_lines(self, all_pairs):
        for pairs in all_pairs:
            for pair in pairwise(pairs):
                self.draw_line(pair[0], pair[1])


def parse_parts(parts):
    return [list(map(int, part.split(","))) for part in parts]


def day14(part_a, void=True):
    all_parts = []
    for l in part_a:
        parts = l.split(" -> ")
        parts = parse_parts(parts)
        all_parts.append(parts)

    grid = Grid(void)
    grid.draw_lines(all_parts)

    count = 0
    while True:
        old_grid = grid.grid.copy()

        if grid.flow_sand():
            count += 1
            break

        if old_grid == grid.grid:
            break
        count += 1

    return count


TEST = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()


def test_part_a():
    assert day14(TEST, True) == 24


def test_part_b():
    assert day14(TEST, False) == 93


if __name__ == "__main__":
    test_part_a()
    submit(day14(lines, True), part="a", day=14, year=2022)

    test_part_b()
    submit(day14(lines, False), part="b", day=14, year=2022)
