from aocd import data, lines, submit

TEST = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".splitlines()


def parse(line):
    return tuple(map(int, line.split(",")))


def touches(c, cubes):
    return sum(1 for s in sides(*c) if s not in cubes)


def sides(x, y, z):
    return {
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    }


def day18(input):
    cubes = set()

    mind = maxd = 0
    for l in input:
        (x, y, z) = parse(l)

        mind = min(mind, x, y, z)
        maxd = max(maxd, x, y, z)

        cubes.add((x, y, z))

    todo = [(mind - 1, mind - 1, mind - 1)]
    seen = set()

    # flood fill the outside of the lava
    while todo:
        here = todo.pop()
        for s in sides(*here) - cubes - seen:
            if all((mind - 1) <= c <= maxd + 1 for c in s):
                todo.append(s)
        seen.add(here)

    a = sum([touches(c, cubes) for c in cubes])
    b = sum((s in seen) for c in cubes for s in sides(*c))

    return a, b


def test_part_a():
    assert day18(TEST) == (64, 58)


if __name__ == "__main__":
    test_part_a()
    a, b = day18(lines)
    submit(a, part="a", day=18, year=2022)
    submit(b, part="b", day=18, year=2022)
