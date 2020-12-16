#!/usr/bin/env python3

with open("input.txt") as file:
    f = file.read().split()
    ws = 25
    for i in range(0, len(f)-ws-1):
        count = 0
        w = f[i:i+ws]
        e = f[i+ws+1]
        aux = []
        for it in w:
            aux.append(int(e) - int(it))
        # print(aux, w, e)
        for m in aux:
            if str(m) not in w:
                count += 1
                # print(e)
        if count == ws:
            print(e)
    # print(f)
