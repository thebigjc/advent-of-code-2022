from aocd import data, submit


def test_data_a():
    assert marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert marker("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11


def test_data_b():
    assert marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert marker("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26


def marker(input: str, l: int) -> int:
    for i in range(l, len(input)):
        if len(set(input[i - l : i])) == l:
            return i


if __name__ == "__main__":
    submit(marker(data, 4), part="a", day=6, year=2022)
    submit(marker(data, 14), part="b", day=6, year=2022)
