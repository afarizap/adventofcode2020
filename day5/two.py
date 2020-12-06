#!/usr/bin/env python3

with open("input.txt") as file:
    f = file.read().split()
    mx = 0
    st = []
    for i in f:
        space = 128
        position = 0
        row = 8
        seat = 0
        for p in i[:7]:
            if p == 'B':
                position += space // 2
            space //= 2
        for s in i[7:]:
            if s == 'R':
                seat += row // 2
            row //= 2
        if mx < position * 8 + seat:
            mx = position * 8 + seat
        st.append(position *8 + seat)
    st.sort()
    cp = st[0]
    for ob in st:
        if ob == cp:
            cp += 1
        else:
            print(cp)
            break
