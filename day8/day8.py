from aocd import lines, submit

TEST = """30373
25512
65332
33549
35390""".splitlines()

tree_lines = lines

trees = []

y_len = len(tree_lines)
x_len = len(tree_lines[0])

visible = {}

def to_coords(i, y_max):
    return (i % y_max, i // y_max)

def is_edge(t, i):
    (x, y) = to_coords(i, y_len)
    if x == 0 or x == x_len - 1 or y == 0 or y == y_len - 1:
        return True

def tree_at(x, y):
    assert x >= 0 and x < x_len
    assert y >= 0 and y < y_len

    return trees[x + y * y_len]

def visible_dir(t, start, end, step, tree_func):
    visible = True
    for i_x in range(start, end, step):
        if tree_func(i_x) >= t:
            visible = False
    return visible

def is_visible(t, i):
    (x, y) = to_coords(i, y_len)

    visible_left = visible_dir(t, 0, x, 1, lambda l: tree_at(l, y))
    visible_right = visible_dir(t, x_len-1, x, -1, lambda l: tree_at(l, y))
    visible_down = visible_dir(t, 0, y, 1, lambda l: tree_at(x, l))
    visible_up = visible_dir(t, y_len-1, y, -1, lambda l: tree_at(x, l))
    
    return visible_left or visible_right or visible_down or visible_up

def score_tree(t, start, end, step, tree_func):
    score = 0
    for i_x in range(start, end, step):
        score += 1
        if tree_func(i_x) >= t:
            break
    return score

def tree_score(t, i):
    (x, y) = to_coords(i, y_len)

    horiz = lambda l: tree_at(l, y)
    vert = lambda l: tree_at(x, l)

    score_left = score_tree(t, x-1, -1, -1, horiz)
    score_right = score_tree(t, x+1, x_len, 1, horiz)
    score_up = score_tree(t, y-1, -1, -1, vert)
    score_down = score_tree(t, y+1, y_len, 1, vert)

    return score_left * score_right * score_down * score_up

for l in tree_lines:
    trees.extend(list(map(int, l)))

best_score = 0
for i, t in enumerate(trees):
    if is_edge(t, i):
        visible[i] = True
    else:
        if is_visible(t, i):
            visible[i] = True
        new_score = tree_score(t, i)
        best_score = max(best_score, new_score)

submit(len(visible), part="a", day=8, year=2022)
submit(best_score, part="b", day=8, year=2022)