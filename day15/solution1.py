#!/usr/bin/env python3
import os

file_dir = os.path.dirname(os.path.abspath(__file__))

result = 0
sequences = list()

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
    result += get_hash(sequence)

print(result)