from aocd import lines, submit
from operator import add, mul, sub, truediv
import sympy

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
    assert day21_part_a(TEST) == 152

def test_part_b():
    assert day21_part_b(TEST) == 301

class Monkey:
    def __init__(self, value=None, l=None, r=None, op=None):
        self.var = None
        self.value = value
        self.left = l
        self.right = r
        self.op_code = op
        self.op = None
        if op:
            match op:
                case "+":
                    self.op = add
                case "-":
                    self.op = sub
                case "*":
                    self.op = mul
                case "/":
                    self.op = truediv
                case "=":
                    self.op = lambda x, y: sympy.Eq(x, y)

    def eval(self, monkeys):
        if self.value is None:
            self.value = self.op(monkeys[self.left].eval(monkeys), monkeys[self.right].eval(monkeys))
        return self.value

def day21_part_a(input):
    monkeys = make_monkeys(input)

    return monkeys["root"].eval(monkeys)

def day21_part_b(input):
    monkeys = make_monkeys(input, True)

    print(f"Root: {monkeys['root'].eval(monkeys)}")

    result = sympy.solve(monkeys["root"].eval(monkeys), monkeys["humn"].value)
    print(result)

    return int(result[0]+0.5)

def make_monkeys(input, part_b=False):
    monkeys = {}
    for l in input:
        name = l[0:4]
        op = l[6:]
        if part_b and name == "humn":
            monkeys[name] = Monkey(value=sympy.Symbol(name))
            continue

        if op[0] in "0123456789":
            monkeys[name] = Monkey(value=int(op))
        else:
            l, op_code, r = op.split()
            if name == "root" and part_b == True:
                op_code = '='

            monkeys[name] = Monkey(l=l, r=r, op=op_code)
    return monkeys   

if __name__ == "__main__":
    test_part_a()
    submit(day21_part_a(lines), part="a", day=21, year=2022)
    test_part_b()
    submit(day21_part_b(lines), part="b", day=21, year=2022)
    