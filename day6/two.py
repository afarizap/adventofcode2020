#!/usr/bin/env python3
with open("input.txt") as file:
    g = file.read().replace('\n\n', ';').replace('\n', ',').split(';')
    a = []
    for s in g:
        ad = s.split(',')
        a.append(ad)
    a[-1].pop()
    m = 0
    for i in a:
        for w in i[0]:
            h = 0
            for l in i:
                if w in l:
                    h +=1
            if h == len(i):
                m += 1
    print(m)
