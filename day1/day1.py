from aocd import lines, submit
from typing import Iterator
import heapq 

def elves(lines: Iterator[str]) -> Iterator[int]:
    s : int = 0
    for l in lines:
        if len(l) == 0:
            yield s
            s = 0
        else:
            s += int(l)

m : int = max(elves(lines))
three : int = sum(heapq.nlargest(3, elves(lines)))

submit(m, part="a", day=1, year=2022)
submit(three, part="b", day=1, year=2022)
