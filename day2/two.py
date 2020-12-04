#!/usr/bin/env python3
with open("input.txt") as f:
    j = 0
    for i in range(1000):
        x = f.readline()
        y = x.split()
        a = y[0].split("-")
        b = y[1].split(":")
        c = y[2]
        m = 0
        if c[int(a[0]) - 1] is b[0]:
            m += 1
        if c[int(a[1]) - 1] is b[0]:
            m += 1
        if m is 1:
            j += 1
        print(a[0], a[1], b[0], c, j)
print(j)
