import itertools
from aocd import lines, submit

TEST = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()

def test_part_a():
    assert day10(TEST).score == 13140

def test_part_b():
    day10(TEST).image_str() == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....""".replace(".", " ").splitlines()

class State:
    def __init__(self):
        self.ip = 0
        self.x = 1
        self.score = 0
        self.image = []

    def image_str(self):
        rows = itertools.batched(self.image, 40)
        return "\n".join(map(lambda row: "".join(row), rows))

    def increment_ip(self):
        col = self.ip % 40

        if self.x in (col-1, col, col+1):
            self.image.append("#")
        else:
            self.image.append(" ")

        self.ip += 1

        if self.ip in (20, 60, 100, 140, 180, 220):                
            self.score += self.ip * self.x
    
    def noop(self):
        self.increment_ip()

    def addx(self, value : int):
        self.increment_ip()
        self.increment_ip()
        self.x += value


def day10(inputs):
    state = State()

    for l in inputs:
        if l.startswith("addx"):
            state.addx(int(l[5:]))
        else:
            state.noop()

    return state
    
if __name__ == "__main__":
    state = day10(lines)
    submit(state.score, part="a", day=10, year=2022)
    print(state.image_str())
