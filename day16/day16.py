from collections import defaultdict
from functools import cache
import itertools
from aocd import lines, submit
from parse import parse


class Valve:
    def __init__(self, name, rate, children):
        self.name = name
        self.rate = int(rate)
        self.children = children


scores = {}
max_score = 0

flows = {}
distances = defaultdict(lambda: 1000)


@cache
def search(valves, time=30, valve="AA", e=False):
    return max(
        [
            flows[v] * (time - distances[valve, v] - 1)
            + search(valves - {v}, time - distances[valve, v] - 1, v, e)
            for v in valves
            if distances[valve, v] < time
        ]
        + [search(valves=valves, time=26) if e else 0]
    )


def day16(input_valves, elephant=False):
    valves = set()

    # "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
    for valve in input_valves:
        (v, t) = valve.split(";")
        (cur_v, rate) = parse("Valve {} has flow rate={}", v)
        children = None
        if t.startswith(" tunnels"):
            children = t[24:].split(", ")
        else:
            children = [t[23:]]
        valves.add(cur_v)
        if rate != "0":
            flows[cur_v] = int(rate)

        for c in children:
            distances[(cur_v, c)] = 1

    for k, i, j in itertools.product(valves, valves, valves):  # floyd-warshall
        distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])

    valves = frozenset(flows)
    if elephant:
        return search(valves, time=26, e=True)
    else:
        return search(valves, time=30)


TEST = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()


def test_part_a():
    assert day16(TEST) == 1651


def test_part_b():
    assert day16(TEST, True) == 1707


if __name__ == "__main__":
    submit(day16(lines), part="a", day=16, year=2022)
    submit(day16(lines, True), part="b", day=16, year=2022)
