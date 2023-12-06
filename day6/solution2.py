#!/usr/bin/env python3
import os

file_dir = os.path.dirname(os.path.abspath(__file__))

result = 1

with open(f"{file_dir}/input") as f:
    times = [int(f.readline().replace(" ", "").split(":")[1])]
    distances = [int(f.readline().replace(" ", "").split(":")[1])]

for index, time in enumerate(times):
    min = 0
    max = 0
    for ms in range(0, time + 1):
        if distances[index] < (time - ms) * ms:
            min = ms
            break
    for ms in range(time + 1, 0, -1):
        if distances[index] < (time - ms) * ms:
            max = ms
            break

    result = max-min+1

print(result)
