from aocd import data, submit
from typing import Iterator
from more_itertools import take

def make_elves(elves: Iterator[str]) -> Iterator[int]:
    for l in elves:
        yield sum(map(int, l.split("\n")))
    
top_3 = take(3, sorted(make_elves(data.split("\n\n")), reverse=True))

submit(top_3[0], part="a", day=1, year=2022)
submit(sum(top_3), part="b", day=1, year=2022)
