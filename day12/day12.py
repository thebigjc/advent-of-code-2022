from aocd import lines, submit

def get_value(input, x, y, width):
    if x>= 0 and y >= 0 and x < width and y < len(input) // width:
        idx = x + y * width
        v = input[idx]
        if v == 'S':
            return 'a', idx
        elif v == 'E':
            return 'z', idx
        return v,idx
    return None, None

def build_graph(input, width):
    graph = []

    deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))

    for y in range(len(input) // width):
        for x in range(width):
            start_val, start_idx = get_value(input, x, y, width)
 
            for d in deltas:
                dest = (x + d[0], y + d[1])
                dest_val, dest_idx = get_value(input, dest[0], dest[1], width)                    
                if not dest_val:
                    continue
                
                if ord(dest_val) - ord(start_val) <= 1:
                    graph.append((dest_idx, start_idx))

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

    dist = [float("Inf")] * len(input)
    dist[end] = 0
    w = 1

    for i in range(len(input)-1):
        for (u,v) in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

    return min(dist[i] for i, x in enumerate(input) if x in start_chars)

if __name__ == "__main__":
    #test_part_a()
    submit(path_len(lines, ['S']), part="a", day=12, year=2022)
    submit(path_len(lines, ['S', 'a']), part="b", day=12, year=2022)