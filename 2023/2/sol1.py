# coding: utf-8
import re

idtotal = 0

with open('input') as f:
    for line in f:
        gameid = int(re.findall(r'Game (\d+)', line)[0])
        reds = max([int(count) for count in re.findall(r'(\d+) red', line)])
        greens = max([int(count) for count in re.findall(r'(\d+) green', line)])
        blues = max([int(count) for count in re.findall(r'(\d+) blue', line)])
        if reds <= 12 and greens <= 13 and blues <= 14:
            idtotal += gameid

print(idtotal)
