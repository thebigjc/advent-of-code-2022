from aocd import lines, submit
from parse import parse

TEST = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def test_total_dirs():
    all_dirs = parse_dirs(TEST.splitlines())

    assert part_a(all_dirs) == 95437

def test_total_dirs():
    all_dirs = parse_dirs(TEST.splitlines())

    assert part_b(all_dirs) == 24933642


class Dir:
    def __init__(self, name : str, parent = None):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def add_dir(self, child):
        self.children.append(child)
    
    def add_file(self, size : int):
        self.size += size

    def total_size(self, max_size: int = 100000):
        return self.size + sum([child.total_size(max_size) for child in self.children])


def parse_dirs(lines : list[str]) -> list[Dir]:
    root = Dir("/")
    cwd = root

    all_dirs = [root]

    for l in lines:
        if l.startswith("$ cd "):
            dir_name = l[5:]
            new_dir = Dir(l[5:], cwd)
            if dir_name == "/":
                cwd = root
            elif dir_name == "..":
                cwd = cwd.parent
            else:
                all_dirs.append(new_dir)
                cwd.add_dir(new_dir)
                cwd = new_dir
        elif p := parse("{:d} {}", l):
            cwd.add_file(p[0])

    return all_dirs

def part_a(dirs : list[Dir]) -> int:
    return sum(d.total_size() for d in dirs if d.total_size() < 100000)

def part_b(all_dirs):
    free_space = 70000000 - max(d.total_size() for d in all_dirs)
    space_needed = 30000000 - free_space

    return min(d.total_size() for d in all_dirs if d.total_size() >= space_needed)

all_dirs = parse_dirs(lines)
s_a = part_a(all_dirs)
s_b = part_b(all_dirs)

submit(s_a, part="a", day=7, year=2022)
submit(s_b, part="b", day=7, year=2022)