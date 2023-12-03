# coding: utf-8
import re

powersum = 0
        
with open('input') as f:
    for line in f:
        maxred = max([int(red) for red in re.findall(r'(\d+) red', line)])
        maxgreen = max([int(green) for green in re.findall(r'(\d+) green', line)])
        maxblue = max([int(blue) for blue in re.findall(r'(\d+) blue', line)])
        powersum += (maxred * maxgreen * maxblue)

print(powersum)
