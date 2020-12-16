#!/usr/bin/env python3

with open("input") as fp:
    f = fp.read().split()
    numbers = []
    onej = 1
    threej = 1
    for i in f:
        numbers.append(int(i))
    numbers.sort()
    new = [numbers[0]]
    numbers.pop(0)
    old = numbers[:]
    for x in numbers:
        # print(x, new[-1])
        if x - new[-1] == 1:
            onej += 1
        else:
            threej += 1
        new.append(old[0])
        old.pop(0)
    print(onej, threej, onej * threej)
