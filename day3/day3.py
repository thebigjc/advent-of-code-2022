from aocd import lines, submit
from itertools import batched


def test_score_a():
    assert score("A") == 27
    assert score("a") == 1


def split(l: str) -> tuple:
    return (set(l[len(l) // 2 :]), set(l[: len(l) // 2]))


def pop_intersections(s) -> str:
    return set.intersection(*map(set, s)).pop()


def score(a):
    s = ord(a)
    if s >= ord("a"):
        s -= ord("a") - 1
    else:
        s -= ord("A") - 27

    return s


if __name__ == "__main__":
    s = sum(map(score, map(pop_intersections, map(split, lines))))

    submit(s, part="a", day=3, year=2022)

    s = sum(map(score, map(pop_intersections, batched(lines, 3))))
    submit(s, part="b", day=3, year=2022)
