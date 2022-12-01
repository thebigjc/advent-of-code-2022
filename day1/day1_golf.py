from aocd import data, submit
from more_itertools import take

top_3 = take(3, sorted(map(lambda x: sum(map(int, x.split("\n"))), data.split("\n\n")), reverse=True))

submit(top_3[0], part="a", day=1, year=2022)
submit(sum(top_3), part="b", day=1, year=2022)
