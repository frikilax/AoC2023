#!/usr/bin/env python3
import os

file_dir = os.path.dirname(os.path.abspath(__file__))

result = 1

with open(f"{file_dir}/input") as f:
    times = [int(time) for time in f.readline().split()[1:]]
    distances = [int(distance) for distance in f.readline().split()[1:]]

for index, time in enumerate(times):
    possible = 0
    for ms in range(0, time + 1):
        if distances[index] < (time - ms) * ms:
            possible += 1

    result *= possible

print(result)
