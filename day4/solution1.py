#!/usr/bin/env python3
import os

file_dir = os.path.dirname(os.path.abspath(__file__))

result = 0
data = list()

with open(f"{file_dir}/input") as f:
    for line in f.readlines():
        line_data = line.replace(":", "|").split('|')[1:]
        filtered_winning = list()
        filtered_actual = list()
        for number in line_data[0].split(' '):
            try:
                filtered_winning.append(int(number, 10))
            except ValueError:
                continue
        for number in line_data[1].split(' '):
            try:
                filtered_actual.append(int(number, 10))
            except ValueError:
                continue

        data.append((filtered_winning, filtered_actual))


for winning, actual in data:
    partial_result = 0
    first = True
    for number in winning:
        if number in actual:
            partial_result = 1 if first else partial_result * 2
            first = False

    result += partial_result

print(data)
print(result)
