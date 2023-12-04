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

        data.append({
            "quantity": 1,
            "winning_nums": filtered_winning,
            "actual_nums": filtered_actual
            })


for index, obj in enumerate(data):
    num_matches = 0
    for number in obj['winning_nums']:
        if number in obj['actual_nums']:
            num_matches += 1

    for next_card in range(1, num_matches + 1):
        if index + next_card < len(data):
            data[index + next_card]['quantity'] += obj['quantity']

for index, card in enumerate(data):
    result += card['quantity']

print(result)
