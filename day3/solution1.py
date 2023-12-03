#!/usr/bin/env python3
import os

file_dir = os.path.dirname(os.path.abspath(__file__))

result = 0
data = list()

def get_special_positions(data):
    reply = list()
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if not data[i][j] in "0123456789.":
                reply.append((i, j))
    return reply

def get_number_positions(special_positions, data):
    reply = list()
    for spe_pos_x, spe_pos_y in special_positions:
        for pos_x in range(spe_pos_x - 1, spe_pos_x + 2):
            adjacent = False
            if pos_x < 0 or pos_x > len(data):
                continue
            for pos_y in range(spe_pos_y - 1, spe_pos_y + 2):
                if pos_y < 0 or pos_y > len(data):
                    continue
                if data[pos_x][pos_y].isdigit() and not adjacent:
                    reply.append((pos_x, pos_y))
                    adjacent = True
                else:
                    adjacent = False
    return reply

def get_numbers(num_positions, data):
    reply = set()
    for x_pos, y_pos in num_positions:
        y_min, y_max = 0, 0
        while y_pos > 0 and (data[x_pos][y_pos-1].isdigit()):
            y_pos -= 1
        y_min = y_pos
        while y_pos < len(data[x_pos]) - 1 and data[x_pos][y_pos+1].isdigit():
            y_pos += 1
        y_max = y_pos
        reply.add((int(data[x_pos][y_min:y_max+1]), x_pos, y_pos))
    return reply


with open(f"{file_dir}/input") as f:
    for line in f.readlines():
        data.append(line.strip('\n'))

spe_positions = get_special_positions(data)
num_positions = get_number_positions(spe_positions, data)
numbers = get_numbers(num_positions, data)

for number in numbers:
    result += number[0]

print(numbers)
print(result)
