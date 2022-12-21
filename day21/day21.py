from aocd import lines, submit
from operator import add, mul, sub, floordiv

TEST = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".splitlines()

def test_part_a():
    assert day21(TEST) == 152


class Monkey:
    def __init__(self, value=None, l=None, r=None, op=None):
        self.value = value
        self.left = l
        self.right = r
        if op:
            match op:
                case "+":
                    self.op = add
                case "-":
                    self.op = sub
                case "*":
                    self.op = mul
                case "/":
                    self.op = floordiv

    def eval(self, monkeys):
        if self.value is None:
            self.value = self.op(monkeys[self.left].eval(monkeys), monkeys[self.right].eval(monkeys))
        return self.value

def day21(input):
    monkeys = {}
    for l in input:
        name = l[0:4]
        op = l[6:]
        if op[0] in "0123456789":
            monkeys[name] = Monkey(value=int(op))
        else:
            l, _, r = op.split()
            monkeys[name] = Monkey(l=l, r=r, op=op[5])

    return monkeys["root"].eval(monkeys)    

if __name__ == "__main__":
    test_part_a()
    submit(day21(lines), part="a", day=21, year=2022)