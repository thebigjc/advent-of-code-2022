from aocd import lines, submit


def test_overlap():
    assert overlap("2-4", "6-8") == 0
    assert overlap("2-8", "3-7") == 5
    assert overlap("6-6", "4-6") == 1
    assert overlap("4-6", "6-6") == 1
    assert overlap("5-7", "7-9") == 1
    assert overlap("2-6", "4-8") == 3


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


def parse_range(r: str) -> tuple[int, int]:
    (a, b) = r.split("-")
    return (int(a), int(b))


def range_set(r: str) -> set[int]:
    (a, b) = parse_range(r)
    return set(range(a, b + 1))


def overlap(a: str, b: str) -> int:
    set_a = range_set(a)
    set_b = range_set(b)

    return len(set_a.intersection(set_b))


if __name__ == "__main__":
    n_a : int = 0
    n_b : int = 0

    for l in lines:
        (a, b) = l.split(",")

        l = overlap(a, b)
        if l == len(a) or l == len(b):
            n_a += 1
        if l > 0:
            n_b += 1

    submit(n_a, part="a", day=4, year=2022)
    submit(n_b, part="b", day=4, year=2022)
