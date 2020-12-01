#!/usr/bin/env python3

with open("input.txt") as f:
    x = f.read().splitlines()
y = x[:]
for i in x:
    for j in y:
        if (str(2020 - int(i) - int(j))) in y:
            print(int(i) * (2020 - int(i) - int(j)) * int(j))
        else:
            continue
