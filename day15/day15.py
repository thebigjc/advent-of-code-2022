from functools import cache
from itertools import pairwise
from aocd import lines, submit
from parse import parse

TEST = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
""".splitlines()


def test_part_a():
    assert day15_a(TEST, 10) == 26


def test_part_b():
    assert day15_b(TEST, 20) == 56000011


def day15_a(sensors_and_beacons, row):
    sensors = []
    beacons = []
    impossible_locations = set()
    for l in sensors_and_beacons:
        (sensor_x, sensor_y, beacon_x, beacon_y) = parse(
            "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", l
        )
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        sensors.append((sensor_x, sensor_y, distance))
        beacons.append((beacon_x, beacon_y))

    for sensor_x, sensor_y, distance in sensors:
        if abs(row - sensor_y) > distance:
            continue
        distance -= abs(row - sensor_y)
        for beacon_x in range(sensor_x - distance, sensor_x + distance + 1):
            impossible_locations.add(beacon_x)

    for beacon_x, beacon_y in beacons:
        if beacon_y == row:
            impossible_locations.discard(beacon_x)

    return len(impossible_locations)

@cache
def overlap(r1, r2):
    return 


def day15_b(sensors_and_beacons, max_coord):
    sensors = []
    beacons = []
    for l in sensors_and_beacons:
        (sensor_x, sensor_y, beacon_x, beacon_y) = parse(
            "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", l
        )
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        sensors.append((sensor_x, sensor_y, distance))
        beacons.append((beacon_x, beacon_y))

    for row in range(max_coord):
        ranges = []

        for sensor_x, sensor_y, distance in sensors:
            if abs(row - sensor_y) > distance:
                continue
            distance -= abs(row - sensor_y)
            ranges.append(
                (max(sensor_x - distance, 0), min(max_coord, sensor_x + distance))
            )

        ranges.sort()

        row_range = (0, 0)
        for r in ranges:
            if r[0] <= min(row_range[1], r[1]):
                row_range = (row_range[0], max(row_range[1], r[1]))
            else:
                return (row_range[1] + 1) * 4000000 + row


if __name__ == "__main__":
#    test_part_a()
#    submit(day15_a(lines, 2000000), part="a", day=15, year=2022)
#    test_part_b()
    submit(day15_b(lines, 4000000), part="b", day=15, year=2022)
