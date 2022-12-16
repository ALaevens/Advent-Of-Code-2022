from vector import Vector2
from math import floor
import re

def manhattan(a: Vector2, b: Vector2):
    return abs(b.x - a.x) + abs(b.y - a.y)

def beacon_ranges(sensor_range, y_level):
    covered_ranges = []
    for sensor in sensor_range:
        range = sensor_range[sensor]

        leftover = range - manhattan(sensor, Vector2(sensor.x, y_level))

        if leftover < 0:
            continue
        
        covered_ranges.append((sensor.x - leftover, sensor.x + leftover))

    return covered_ranges

def consolidate(ranges: list[tuple]):
    ranges.sort(key=lambda x: x[0])
    
    shortened = []
    while len(ranges) > 1:
        low = ranges.pop(0)
        next = ranges[0]

        if next[0] > low[1]+1: # ranges do not overlap
            shortened.append(low)
            continue

        ranges[0] = (low[0], max(low[1], next[1]))

    shortened += ranges

    return shortened

with open("input.txt") as f:
    sensor_range = {}

    for line in f:
        line = line.strip()

        x_parts = re.findall("x=-*\d+", line)
        y_parts = re.findall("y=-*\d+", line)

        sensor = Vector2(int(x_parts[0][2:]), int(y_parts[0][2:]))
        beacon = Vector2(int(x_parts[1][2:]), int(y_parts[1][2:]))

        sensor_range[sensor] = manhattan(sensor, beacon)

    percent_done = 0
    for i in range(0, 4000001):
        covered_ranges = beacon_ranges(sensor_range, i)
        covered_ranges = consolidate(covered_ranges)

        now_percent = floor((i / 4000000) * 100)
        if now_percent > percent_done:
            percent_done = now_percent
            print(f"{now_percent}%")

        if len(covered_ranges) > 1:
            print((covered_ranges[0][1]+1) * 4000000 + i)
            break

    
