from aocd import lines, submit
import networkx as nx

def get_value(input, x, y, width):
    if x>= 0 and y >= 0 and x < width and y < len(input) // width:
        v = input[x + y * width]
        if v == 'S':
            return 'a'
        elif v == 'E':
            return 'z'
        return v
    return None

def build_graph(input, width):
    graph = nx.DiGraph()
    graph.add_nodes_from([(x, y) for x in range(width) for y in range(len(input) // width)])

    deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))

    for y in range(len(input) // width):
        for x in range(width):
            start_val = get_value(input, x, y, width)
            start = (x,y)
            for d in deltas:
                dest = (x + d[0], y + d[1])
                dest_val = get_value(input, dest[0], dest[1], width)                    
                if not dest_val:
                    continue
                if ord(dest_val) - ord(start_val) <= 1:
                    graph.add_edge(start, dest)

    return graph

TEST = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()

def test_part_a():
    assert(path_len(TEST, ['S']) == 31)
    assert(path_len(TEST, ['S', 'a']) == 29)

def path_len(hills, start_chars):
    width = len(hills[0])
    input = "".join(hills)
    graph = build_graph(input, width)
    
    end = input.index('E')
    end_pos = (end % width, end // width)

    lens = []

    for start_char in start_chars:
        starts = [i for i, x in enumerate(input) if x == start_char]
        print(f"Found {len(starts)} starts for {start_char}")
        n = 0
        for start in starts:
            start_pos = (start % width, start // width)
            path = None

            try:
                path = nx.shortest_path(graph, source=start_pos, target=end_pos)
            except:
                pass

            if path:
                lens.append(len(path)-1)
    
    return min(lens)


if __name__ == "__main__":
    submit(path_len(lines, ['S']), part="a", day=12, year=2022)
    submit(path_len(lines, ['S', 'a']), part="b", day=12, year=2022)