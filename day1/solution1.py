#!/usr/bin/env python3

result = 0

with open("./input") as f:
    for line in f.readlines():
        filtered = ''.join(filter(str.isdigit, line))
        num = int(filtered[0] + filtered[-1], 10)
        print(f"{line} -> {num}")
        result += num

print(result)