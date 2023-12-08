#!/usr/bin/env python3
import os

file_dir = os.path.dirname(os.path.abspath(__file__))

result = 0
instructions = ""
map = dict()
position = ''

def navigate(instructions, position, steps, map):
    print(f"at {position}")
    if not instructions or position == "ZZZ":
        return position, steps
    elif instructions[0] == 'L':
        return navigate(instructions[1:], map[position][0], steps+1, map)
    else:
        return navigate(instructions[1:], map[position][1],steps+1, map)

with open(f"{file_dir}/input") as f:
    instructions = f.readline().strip()
    for line in f.readlines():
        if not line.strip():
            continue
        input, outputs = line.split('=')
        left, right = outputs.replace('(', '').replace(')', '').split(',')
        map[input.strip()] = (left.strip(), right.strip())

position = "AAA"

steps = 0
while position != "ZZZ":
    position, steps = navigate(instructions, position, steps, map)
    print(position)

print(steps)
