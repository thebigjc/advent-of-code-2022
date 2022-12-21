from aocd import numbers, submit

TEST = tuple(map(int, """1
2
-3
3
-2
0
4""".splitlines()))

def day20(input, mix=1, key=1):
    numbers = list(map(lambda x: x * key, input))
    indices = list(range(len(input)))

    for i in indices * mix:
        idx = indices.index(i)
        indices.pop(idx)
        indices.insert((idx+numbers[i]) % len(indices), i)            
        
    zero = indices.index(numbers.index(0))
    return sum(numbers[indices[(zero+offset) % len(numbers)]] for offset in [1000,2000,3000])
    

def test_part_a():
    assert day20(TEST) == 3

def test_part_b():
    assert day20(TEST, 10, 811589153) == 1623178306

if __name__ == '__main__':
    test_part_a()
    submit(day20(numbers), part="a", day=20, year=2022)
    test_part_b()
    submit(day20(numbers, 10, 811589153), part="b", day=20, year=2022)