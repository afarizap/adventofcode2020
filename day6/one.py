#!/usr/bin/env python3
with open("input.txt") as file:
    f = file.read().replace('\n\n', ';').replace('\n', '').split(';')
    sm = 0
    for i in f:
        tmp = len(set(i))
        sm += tmp
    print(sm)
