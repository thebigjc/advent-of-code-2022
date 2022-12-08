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

visible_trees = {}


def to_coords(idx, y_max):
    return (idx % y_max, idx // y_max)


def is_edge(idx):
    (x_idx, y_idx) = to_coords(idx, y_len)
    return x_idx == 0 or x_idx == x_len - 1 or y_idx == 0 or y_idx == y_len - 1


def tree_at(x_idx, y_idx):
    assert 0 < x_idx < x_len
    assert 0 < y_idx < y_len

    return trees[x_idx + y_idx * y_len]


def visible_dir(height, start, end, step, tree_func):
    visible = True
    for i_x in range(start, end, step):
        if tree_func(i_x) >= height:
            visible = False
    return visible


def is_visible(height, idx):
    (x_idx, y_idx) = to_coords(idx, y_len)

    visible_left = visible_dir(height, 0, x_idx, 1, lambda l: tree_at(l, y_idx))
    visible_right = visible_dir(height, x_len - 1, x_idx, -1, lambda l: tree_at(l, y_idx))
    visible_down = visible_dir(height, 0, y_idx, 1, lambda l: tree_at(x_idx, l))
    visible_up = visible_dir(height, y_len - 1, y_idx, -1, lambda l: tree_at(x_idx, l))

    return visible_left or visible_right or visible_down or visible_up


def score_tree(height, start, end, step, tree_func):
    score = 0
    for i_x in range(start, end, step):
        score += 1
        if tree_func(i_x) >= height:
            break
    return score


def tree_score(height, idx):
    (x_idx, y_idx) = to_coords(idx, y_len)

    horiz = lambda l: tree_at(l, y_idx)
    vert = lambda l: tree_at(x_idx, l)

    score_left = score_tree(height, x_idx - 1, -1, -1, horiz)
    score_right = score_tree(height, x_idx + 1, x_len, 1, horiz)
    score_up = score_tree(height, y_idx - 1, -1, -1, vert)
    score_down = score_tree(height, y_idx + 1, y_len, 1, vert)

    return score_left * score_right * score_down * score_up


for l in tree_lines:
    trees.extend(list(map(int, l)))

best_score = 0
for i, t in enumerate(trees):
    if is_edge(i):
        visible_trees[i] = True
    else:
        if is_visible(t, i):
            visible_trees[i] = True
        new_score = tree_score(t, i)
        best_score = max(best_score, new_score)

submit(len(visible_trees), part="a", day=8, year=2022)
submit(best_score, part="b", day=8, year=2022)
