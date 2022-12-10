from math import prod
import time

from aocd import lines, submit


TEST = """30373
25512
65332
33549
35390""".splitlines()


def to_coords(idx, y_max):
    return (idx % y_max, idx // y_max)


def is_edge(idx, x_len, y_len):
    (x_idx, y_idx) = to_coords(idx, y_len)
    return x_idx == 0 or x_idx == x_len - 1 or y_idx == 0 or y_idx == y_len - 1


def tree_at(x_idx, y_idx, y_len, trees):
    return trees[x_idx + y_idx * y_len]


def visible_dir(height, start, end, step, tree_func):
    visible = True
    for i_x in range(start, end, step):
        if tree_func(i_x) >= height:
            visible = False
    return visible


def is_visible(trees, height, idx, x_len, y_len):
    (x_idx, y_idx) = to_coords(idx, y_len)

    def horiz(x_idx):
        return tree_at(x_idx, y_idx, y_len, trees)

    def vert(y_idx):
        return tree_at(x_idx, y_idx, y_len, trees)

    visible_left = visible_dir(height, 0, x_idx, 1, horiz)
    visible_right = visible_dir(height, x_len - 1, x_idx, -1, horiz)
    visible_down = visible_dir(height, 0, y_idx, 1, vert)
    visible_up = visible_dir(height, y_len - 1, y_idx, -1, vert)

    return any((visible_left, visible_right, visible_down, visible_up))


def score_tree(height, start, end, step, tree_func):
    score = 0
    for i_x in range(start, end, step):
        score += 1
        if tree_func(i_x) >= height:
            break
    return score


def tree_score(trees, height, idx, x_len, y_len):
    (x_idx, y_idx) = to_coords(idx, y_len)

    def horiz(x_idx):
        return tree_at(x_idx, y_idx, y_len, trees)

    def vert(y_idx):
        return tree_at(x_idx, y_idx, y_len, trees)

    score_left = score_tree(height, x_idx - 1, -1, -1, horiz)
    score_right = score_tree(height, x_idx + 1, x_len, 1, horiz)
    score_up = score_tree(height, y_idx - 1, -1, -1, vert)
    score_down = score_tree(height, y_idx + 1, y_len, 1, vert)

    return prod((score_left, score_right, score_down, score_up))

def test_day8():
    assert day8(TEST) == (21, 8)

def day8(tree_lines):
    trees = []

    y_len = len(tree_lines)
    x_len = len(tree_lines[0])

    for l in tree_lines:
        trees.extend(list(map(int, l)))

    part_a = sum(
        1
        for i, t in enumerate(trees)
        if is_edge(i, x_len, y_len) or is_visible(trees, t, i, x_len, y_len)
    )
    part_b = max(
        tree_score(trees, t, i, x_len, y_len)
        for i, t in enumerate(trees)
        if not is_edge(i, x_len, y_len)
    )
    return part_a, part_b


if __name__ == "__main__":
    t1 = time.perf_counter()
    part_a, part_b = day8(lines)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")

    submit(part_a, part="a", day=8, year=2022)
    submit(part_b, part="b", day=8, year=2022)
