# coding: utf-8
import re

total = 0
with open('input') as f:
    for line in f:
        results = re.findall(r'\d', line)
        d1, d2 = results[0], results[-1]
        total += int(d1 + d2)
        
print(total)
