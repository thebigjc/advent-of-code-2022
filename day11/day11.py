from itertools import batched
import math
from time import monotonic

from aocd import lines, submit
from parse import parse

TEST = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".splitlines()


class Monkey:
    def __init__(self, n, items, op, operand, test, if_true, if_false):
        self.n = n
        self.items = items
        match (op, operand):
            case ("*", "old"):
                self.op = lambda x: x * x
            case ("*", value):
                self.op = lambda x: x * int(value)
            case ("+", value):
                self.op = lambda x: x + int(value)

        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0

    def inspect(self, monkeys, test_prods, reduce_worry=True):
        for item in self.items:
            self.inspected += 1
            item = self.op(item)
            if reduce_worry:
                item //= 3

            new_monkey = self.if_false
            if (item % self.test) == 0:
                new_monkey = self.if_true

            assert new_monkey != self.n
            monkeys[new_monkey].items.append(item % test_prods)

        self.items = []


def top_monkeys(lines, rounds, reduce_worry=True):
    monkeys = []

    n = 0
    test_prods = 1
    for monkey in batched(lines, 7):
        items = list(map(int, parse("  Starting items: {}", monkey[1])[0].split(", ")))
        (op, operand) = parse("  Operation: new = old {} {}", monkey[2])
        test = parse("  Test: divisible by {:d}", monkey[3])[0]
        test_prods *= test
        if_true = parse("    If true: throw to monkey {:d}", monkey[4])[0]
        if_false = parse("    If false: throw to monkey {:d}", monkey[5])[0]
        monkeys.append(Monkey(n, items, op, operand, test, if_true, if_false))
        n += 1

    for i in range(rounds):
        start = monotonic()
        if i % 100 == 0:
            print(f"Starting round {i}")
        for monkey in monkeys:
            monkey.inspect(monkeys, test_prods, reduce_worry)

        if i % 100 == 0:
            print(f"Round {i} took {monotonic()-start} seconds")

    return math.prod(sorted(map(lambda x: x.inspected, monkeys), reverse=True)[0:2])


def test_monkeys():
    assert top_monkeys(TEST, 20) == 10605
    assert top_monkeys(TEST, 10000, False) == 2713310158


if __name__ == "__main__":
    test_monkeys()

    submit(top_monkeys(lines, 20), part="a", day=11, year=2022)
    submit(top_monkeys(lines, 10000, False), part="b", day=11, year=2022)
