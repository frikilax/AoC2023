#!/usr/bin/env python3
import os

file_dir = os.path.dirname(os.path.abspath(__file__))

result = 0
seeds = list()
maps = list()

with open(f"{file_dir}/input") as f:
    _endofmap = False
    current_map = list()
    line = f.readline().split()[1:]
    for index, seed in enumerate(line[::2]):
        seed = int(seed)
        range = int(line[index*2+1])
        seeds.append({"start": seed, "range": range})
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

def is_in_seeds(value, seeds):
    for seed in seeds:
        if value >= seed['start'] and value <= seed['start'] + seed['range'] - 1:
            return True
    return False

def find_seed_from_location(location, maps):
    # reverse find sources from destinations
    number = location
    for m in reversed(maps):
        for remap in m:
            if number >= remap['dest'] and number <= remap['dest'] + remap['range'] - 1:
                number = remap['source'] - remap['dest'] + number
                break
    return number

location = 0
while not is_in_seeds(find_seed_from_location(location, maps), seeds):
    location += 1
    continue

print(location)
