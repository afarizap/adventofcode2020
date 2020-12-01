#!/usr/bin/env python3

with open("input.txt") as f:
    x = f.read().splitlines()
y = x[:]
for i in x:
    if (str(2020 - int(i))) in y:
        print(int(i) * (2020 - int(i)))
    else:
        continue
