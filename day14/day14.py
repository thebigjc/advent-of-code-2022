from aocd import lines, submit
from itertools import pairwise
from collections import defaultdict

class Grid:
    def __init__(self):
        self.grid = {}
        self.grid[(500, 0)] = "+"
        self.min_x = 500
        self.max_x = 500
        self.max_y = 0

    def add_rock(self, x, y):
        self.grid[(x, y)] = "#"
        if x < self.min_x:
            self.min_x = x
        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y

    def is_air(self, x, y):
        return (x, y) not in self.grid

    def flow_sand(self):
        # Start at 500,0, and flow down until we hit something
        x, y = 500, 0
        while x >= self.min_x and x <= self.max_x and y <= self.max_y:
            if self.is_air(x, y+1):
                y += 1
                continue
            if self.grid[(x, y+1)] in ("#", "o"):
                if self.is_air(x-1, y+1): # left and down
                    x -= 1
                    y += 1
                    continue
                if self.is_air(x+1, y+1): # right and down
                    x += 1
                    y += 1
                    continue
                self.grid[(x, y)] = "o"
                break

    def draw_line(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1

            for y in range(y1, y2+1):
                self.add_rock(x1, y)
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                self.add_rock(x, y1)
    
    def draw_lines(self, all_pairs):
        for pairs in all_pairs:
            for pair in pairwise(pairs):
                self.draw_line(pair[0], pair[1])


def parse_parts(parts):
    return [list(map(int, part.split(","))) for part in parts]

#        if len(part) == 1:
#            draw_line(part[0], grid)
#        else:
#            draw_line(part[0], grid)
#            draw_line(part[1], grid)

def day14_a(part_a):
    all_parts = []
    for l in part_a:
        parts = l.split(" -> ")
        parts = parse_parts(parts)
        all_parts.append(parts)
    
    grid = Grid()
    grid.draw_lines(all_parts)

    count = 0
    while True:
        old_grid = grid.grid.copy()
        grid.flow_sand()
        if old_grid == grid.grid:
            break
        count += 1
    
    return count

TEST = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

def test_part_a():
    assert(day14_a(TEST) == 24)

if __name__ == "__main__":
    test_part_a()
    #print(day14_a(lines))