#!/usr/bin/env python3
import os

file_dir = os.path.dirname(os.path.abspath(__file__))

locations = list()
seeds = list()
maps = list()

with open(f"{file_dir}/input") as f:
    _endofmap = False
    current_map = list()
    seeds = [int(seed) for seed in f.readline().split()[1:]]
    for line in f.readlines():
        line = line.strip()
        if not line:
            _endofmap = True
            if current_map:
                maps.append(current_map)
            continue
        if _endofmap:
            current_map = list()
            _endofmap = False
            continue

        dest, source, map_range = [int(number) for number in line.split()]

        current_map.append({
            "dest": dest,
            "source": source,
            "range": map_range,
        })

if current_map:
    maps.append(current_map)

for seed in seeds:
    number = seed
    for m in maps:
        for remap in m:
            if number >= remap['source'] and number <= remap['source'] + remap['range'] - 1:
                number = remap['dest'] - remap['source'] + number
                break
    locations.append(number)

print(min(locations))
