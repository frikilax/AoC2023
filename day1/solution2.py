#!/usr/bin/env python3

result = 0

def calibrate(input: str) -> str:
    tokens = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
    }
    for token, number in tokens.items():
        input = input.replace(token, token[0] + str(number) + token[-1])
    return input


with open("./input") as f:
    for line in f.readlines():
        calibrated = calibrate(line)
        filtered = ''.join(filter(str.isdigit, calibrated))
        num = int(filtered[0] + filtered[-1], 10)
        print(f"{line} -> {num}")
        result += num

print(result)
