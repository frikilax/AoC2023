#!/usr/bin/env python3
import os

file_dir = os.path.dirname(os.path.abspath(__file__))

card_mapping = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}
games = list()
scored_games = list()
result = 0

def parse_hand(hand):
    parsed = dict()
    for card in hand:
        parsed[card] = parsed.get(card, 0) + 1
    return parsed

def score_hand(hand):
    score = 0
    counts = parse_hand(hand).values()
    if 5 in counts:
        score = 7
    elif 4 in counts:
        score = 6
    elif 3 in counts and 2 in counts:
        score = 5
    elif 3 in counts:
        score = 4
    elif len([x for x in counts if x == 2]) == 2:
        score = 3
    elif 2 in counts:
        score = 2
    else:
        score = 1
    for card in hand:
        score = score * 100 + card_mapping[card]
    return score


with open(f"{file_dir}/input") as f:
    for line in f.readlines():
        games.append(line.split())

for game in games:
    scored_games.append({
        "game": game,
        "score": score_hand(game[0])
        })

scored_games.sort(key=lambda x: x["score"])
for index, scored_game in enumerate(scored_games):
    result += int(scored_game["game"][1]) * (index + 1)

print(result)
