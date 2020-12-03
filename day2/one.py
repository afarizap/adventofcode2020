#!/usr/bin/env python3
with open("input.txt") as f:
    j = 0
    for i in range(1000):
        x = f.readline()
        y = x.split()
        a = y[0].split("-")
        b = y[1].split(":")
        c = y[2]
        d = c.count(b[0])
        if int(a[0]) <= d <= int(a[1]):
            j += 1
        # print(a[0], a[1], b[0], c, d, j)
print(j)
