#!/usr/bin/env python3
import os

file_dir = os.path.dirname(os.path.abspath(__file__))

data = list()

def extrapolate(suite):
    new_suite = list()
    for index in range(len(suite)-1, 0, -1):
        new_suite.insert(0, suite[index] - suite[index-1])
    if set(new_suite) == set([0]):
        return suite[0]
    else:
        return suite[0] - extrapolate(new_suite)


with open(f"{file_dir}/input") as f:
    for line in f.readlines():
        data.append([int(num) for num in line.split()])

print(sum([extrapolate(suite) for suite in data]))
