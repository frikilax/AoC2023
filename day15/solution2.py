#!/usr/bin/env python3
import os
from collections import OrderedDict

file_dir = os.path.dirname(os.path.abspath(__file__))

result = 0
sequences = list()
boxes = [OrderedDict() for x in range(0, 256)]

def get_hash(sequence):
    hash = 0
    for c in sequence:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash

with open(f"{file_dir}/input") as f:
    sequences = f.readline().strip().split(',')

for sequence in sequences:
    hash = get_hash(sequence.split('=')[0].replace('-', ''))
    if '-' in sequence:
        boxes[hash].pop(sequence.replace('-', ''), None)
    if '=' in sequence:
        label, focal_length = sequence.split('=')
        boxes[hash][label] = int(focal_length)

for index, box in enumerate(boxes):
    for lens_index, (label, focus) in enumerate(box.items()):
        result += (1 + index) * (lens_index + 1) * focus

print(boxes)
print(result)