import aocd
from more_itertools import take

data = aocd.get_data(day=1, year=2022)

top_3 = take(
    3,
    sorted(
        map(lambda x: sum(map(int, x.split("\n"))), data.split("\n\n")), reverse=True
    ),
)

aocd.submit(top_3[0], part="a", day=1, year=2022)
aocd.submit(sum(top_3), part="b", day=1, year=2022)
