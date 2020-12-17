#!/usr/bin/env python3

with open('input') as fl:
    f = fl.read().split()
    moves = []
    for _ in f:
        moves.append([_[0], int(_[1:])])
    x = 0
    y = 0
    way = 1
    ways = ['N', 'E', 'S', 'W']
    for i in moves:
        if i[0] == 'N':
            y += i[1]
        if i[0] == 'S':
            y -= i[1]
        if i[0] == 'E':
            x += i[1]
        if i[0] == 'W':
            x -= i[1]
        if i[0] == 'L':
            way -= i[1]//90
            if way < 0:
                way += 4
        if i[0] == 'R':
            way += i[1]//90
            if way > 3:
                way -= 4
        if i[0] == 'F':
            if ways[way] == 'N':
                y += i[1]
            if ways[way] == 'S':
                y -= i[1]
            if ways[way] == 'E':
                x += i[1]
            if ways[way] == 'W':
                x -= i[1]
    print(abs(abs(x) + abs(y)))
