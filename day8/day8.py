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

def is_visible(t, i):
    (x, y) = to_coords(i, y_len)

    visible_left = True
    for i_x in range(x):
        if tree_at(i_x, y) >= t:
            visible_left = False

    visible_right = True
    for i_x in range(x_len-1, x, -1):
        if tree_at(i_x, y) >= t:
            visible_right = False

    visible_down = True
    for i_y in range(y):
        if tree_at(x, i_y) >= t:
            visible_down = False

    visible_up = True
    for i_y in range(y_len-1, y, -1):
        if tree_at(x, i_y) >= t:
            visible_up = False
    
    return visible_left or visible_right or visible_down or visible_up

def score_tree(t, x, y, start, end, step, tree_func):
    score = 0
    for i_x in range(start, end, step):
        score += 1
        if tree_func(i_x) >= t:
            break
    return score

def tree_score(t, i):
    (x, y) = to_coords(i, y_len)

    score_left = score_tree(t, x, y, x-1, -1, -1, lambda l: tree_at(l, y))
    score_right = score_tree(t, x, y, x+1, x_len, 1, lambda l: tree_at(l, y))
#    score_right = score_tree(t, x, y, x+1, x_len, 1, lambda l: tree_at(l, y))
#    score_right = score_tree(t, x, y, x+1, x_len, 1, lambda l: tree_at(l, y))

    score_up = 0
    for i_y in range(y-1, -1, -1):
        score_up += 1
        if tree_at(x, i_y) >= t:
            break

    score_down = 0
    for i_y in range(y+1, y_len, 1):
        score_down += 1
        if tree_at(x, i_y) >= t:
            break
    
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
    
print(len(visible))
print(best_score)

submit(len(visible), part="a", day=8, year=2022)
submit(best_score, part="b", day=8, year=2022)