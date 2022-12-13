import functools
from aocd import data, submit

TEST = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l > r:
            return 0
        if l < r:
            return 1
        return -1

    if isinstance(l, list) and isinstance(r, list):
        for i in range(min(len(l), len(r))):
            c = compare(l[i], r[i])
            if c == -1:
                continue
            return c
        if len(l) == len(r):
            return -1

        if len(l) < len(r):
            return 1

        if len(l) > len(r):
            return 0
    elif isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])
    elif isinstance(r, list) and isinstance(l, int):
        return compare([l], r)
    else:
        raise Exception(f"Unknown types: {type(l)} {type(r)}")


def day13_a(part_a):
    pairs = part_a.split("\n\n")

    score = 0

    for i, p in enumerate(pairs):
        (left, right) = p.splitlines()
        (left, right) = (eval(left), eval(right))

        score += (i + 1) * compare(left, right)

    return score


def proper_compare(l, r):
    c = compare(l, r)
    if c == 0:
        return 1
    if c == 1:
        return -1
    return 0


def day13_b(part_b):
    lines = list(filter(lambda x: len(x.strip()) > 0, part_b.split("\n")))
    lines.extend(["[[2]]", "[[6]]"])
    lines = sorted(map(eval, lines), key=functools.cmp_to_key(proper_compare))

    return (lines.index([[2]]) + 1) * (lines.index([[6]]) + 1)


def test_part_a():
    assert day13_a(TEST) == 13


def test_part_b():
    assert day13_b(TEST) == 140


if __name__ == "__main__":
    submit(day13_a(data), part="a", day=13, year=2022)
    submit(day13_b(data), part="b", day=13, year=2022)
