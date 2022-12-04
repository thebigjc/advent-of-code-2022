from aocd import lines, submit


def test_overlap():
    assert overlap(range_set("2-4"), range_set("6-8")) == 0
    assert overlap(range_set("2-8"), range_set("3-7")) == 5
    assert overlap(range_set("6-6"), range_set("4-6")) == 1
    assert overlap(range_set("4-6"), range_set("6-6")) == 1
    assert overlap(range_set("5-7"), range_set("7-9")) == 1
    assert overlap(range_set("2-6"), range_set("4-8")) == 3


def test_parse_range():
    assert parse_range("1-2") == (1, 2)
    assert parse_range("2-4") == (2, 4)
    assert parse_range("4-6") == (4, 6)
    assert parse_range("6-6") == (6, 6)


def test_range_set():
    assert range_set("1-2") == {1, 2}
    assert range_set("2-4") == {2, 3, 4}
    assert range_set("4-6") == {4, 5, 6}
    assert range_set("6-6") == {6}


def parse_range(ranges: str) -> tuple[int, int]:
    (range_a, range_b) = ranges.split("-")
    return (int(range_a), int(range_b))


def range_set(range_str: str) -> set[int]:
    (range_a, range_b) = parse_range(range_str)
    return set(range(range_a, range_b + 1))


def overlap(range_set_a: set[int], range_set_b: set[int]) -> int:
    return len(range_set_a.intersection(range_set_b))


if __name__ == "__main__":
    n_a: int = 0
    n_b: int = 0

    for l in lines:
        (a, b) = l.split(",")

        set_a = range_set(a)
        set_b = range_set(b)

        l = overlap(set_a, set_b)
        if l == len(set_a) or l == len(set_b):
            n_a += 1
        if l > 0:
            n_b += 1

    submit(n_a, part="a", day=4, year=2022)
    submit(n_b, part="b", day=4, year=2022)
