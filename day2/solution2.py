#!/usr/bin/env python3
import os
import re

file_dir = os.path.dirname(os.path.abspath(__file__))

result = 0

def parse_sets(line):
    for delim in [';', ':']:
        line = "|".join(line.split(delim))
    return line.split('|')

def parse_game(string):
    found = re.findall(r"Game ([0-9]+)", string)
    return int(found[0])

def parse_values(string):
    found = re.findall(r"([0-9]+) red", string)
    red = int(found[0]) if found else 0
    found = re.findall(r"([0-9]+) green", string)
    green = int(found[0]) if found else 0
    found = re.findall(r"([0-9]+) blue", string)
    blue = int(found[0]) if found else 0
    return (red, green, blue)

def get_highest_set_values(string_sets):
    partial = (0,0,0)
    for string_set in string_sets:
        parsed_set = parse_values(string_set)
        partial = (max(partial[0], parsed_set[0]), max(partial[1], parsed_set[1]), max(partial[2], parsed_set[2]))
    return partial


with open(f"{file_dir}/input") as f:
    for line in f.readlines():
        split_line = parse_sets(line)
        values = get_highest_set_values(split_line[1:])
        result += values[0] * values[1] * values[2]

print(result)