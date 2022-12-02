from aocd import lines, submit

def test_draw_rock():
    assert score_b("A", "Y") == 4

def test_lose_paper():
    assert score_b("B", "X") == 1

def test_win_scissors():
    assert score_b("C", "Z") == 7

score_map = {"A": 1, # Rock
                "B": 2, # Scissors
                "C": 3, # Paper
                "X": 1, # Rock
                "Y": 2, # Scissors
                "Z": 3} # Paper

win_map = {
    (1, 1): 3, # Rock vs Rock
    (1, 2): 0, # Rock vs. Paper
    (1, 3): 6, # Rock vs. Scissors
    (2, 1): 6, # Paper vs. Rock
    (2, 2): 3, # Paper vs. Paper
    (2, 3): 0, # Paper vs. Scissors
    (3, 1): 0, # Scissors vs. Rock
    (3, 2): 6, # Scissors vs. Paper
    (3, 3): 3, # Scissors vs. Scissors
}

strategy_map = {
    (1, 1): "Z", # Rock Lose = Scissors
    (1, 2): "X", # Rock Draw = Rock
    (1, 3): "Y", # Rock Win = Paper
    (2, 1): "X", # Paper Lose = Rock
    (2, 2): "Y", # Paper Draw = Paper
    (2, 3): "Z", # Paper Win = Scissors
    (3, 1): "Y", # Scissors Lose = Paper
    (3, 2): "Z", # Scissors Draw = Scissors
    (3, 3): "X", # Scissors Win = Rock
}

def score(a):
    return score_map[a]

def win(a, b):
    a_s = score(a)
    b_s = score(b)

    return win_map[(b_s, a_s)]

def strategy(a, b):
    a_s = score(a)
    b_s = score(b)

    return strategy_map[(a_s,b_s)]

a_total = 0
b_total = 0

def score_a(a, b):
    s = score(b)
    w = win(a, b)
    return s + w

def score_b(a, b):
    st = strategy(a, b)
    s = score(st)
    w = win(a, st)

    print(f"{a} {b} {st} {s} {w}: {s+w}")

    return s + w

for l in lines:
    (a, b) = l.split()

    a_total += score_a(a, b)
    b_total += score_b(a, b)
    
submit(a_total, part="a", day=2, year=2022)
submit(b_total, part="b", day=2, year=2022)
