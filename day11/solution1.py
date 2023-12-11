#!/usr/bin/env python3
import os

file_dir = os.path.dirname(os.path.abspath(__file__))

map = list()
stars = list()
result = 0

def expand_universe(_map):
    new_map = list()

    for y in range(0, len(_map[0])):
        for x in range(0, len(_map)):
            if y == 0:
                new_map.append(list())
            new_map[x].append(_map[x][y])

        expand = True
        for x in range(0, len(_map)):
            if _map[x][y] == '#':
                expand = False
        if expand:
            for x in range(0, len(_map)):
                new_map[x].append('.')

    x = 0
    while x < len(new_map):
        if '#' not in new_map[x]:
            new_map.insert(x, new_map[x])
            x += 1
        x += 1

    return new_map


with open(f"{file_dir}/input") as f:
    for line in f.readlines():
        map.append([c for c in line.strip()])

map = expand_universe(_map=map)

for x, line in enumerate(map):
    for y, char in enumerate(line):
        if char == "#":
            stars.append((x, y))

for star_number, star in enumerate(stars):
    for other_star in stars[star_number+1:]:
        distance = abs(other_star[0] - star[0]) + abs(other_star[1] - star[1])
        result += distance

print(result)