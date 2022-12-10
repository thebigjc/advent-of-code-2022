import itertools
import operator
from aocd import lines, submit

TEST_A = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()

TEST_B = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".splitlines()

START = (0, 0)


def test_part_a():
    assert day9(TEST_A, 1) == 13


def test_part_b():
    assert day9(TEST_B, 9) == 36


def day9(inputs, knots):
    rope = [list(START) for i in range(knots + 1)]

    locations = set((START,))

    for line in inputs:
        for pair in itertools.pairwise(rope):
            assert abs(pair[0][0] - pair[1][0]) <= 1
            assert abs(pair[0][1] - pair[1][1]) <= 1

        (direction, steps) = (line[0], int(line[1:]))

        delta = (0, 0)

        match direction:
            case "U":
                delta = (0, 1)
            case "D":
                delta = (0, -1)
            case "L":
                delta = (-1, 0)
            case "R":
                delta = (1, 0)

        for i in range(steps):
            head = rope[0]
            tail = tuple(rope[-1])

            (head[0], head[1]) = (head[0] + delta[0], head[1] + delta[1])
            for pair in itertools.pairwise(rope):
                start = pair[0]
                knot = pair[1]
                dx = start[0] - knot[0]
                dy = start[1] - knot[1]

                if dx == 0 or dy == 0:
                    if abs(dx) > 1:
                        knot[0] += 1 if dx > 0 else -1

                    if abs(dy) > 1:
                        knot[1] += 1 if dy > 0 else -1

                elif abs(dx) + abs(dy) > 2:
                    knot[0] += 1 if dx > 0 else -1
                    knot[1] += 1 if dy > 0 else -1

            if rope[-1][0] != tail[0] or rope[-1][1] != tail[1]:
                locations.add(tuple(rope[-1]))

    return len(locations)


if __name__ == "__main__":
    submit(day9(lines, 1), part="a", day=9, year=2022)
    submit(day9(lines, 9), part="b", day=9, year=2022)
