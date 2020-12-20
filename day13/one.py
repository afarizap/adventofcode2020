#!/usr/bin/env python3

with open("input") as fl:
    f = fl.read().split()
    t_stamp = int(f[0])
    bus_ids = f[1].split(',')
    m = 110000000
    for i in bus_ids:
        if i != 'x':
            n = int(i)
            x = t_stamp // n
            x *= n
            if t_stamp % n == 0:
                m = x
                print(m, "time zero")
                break
            s = x + n
            s -= t_stamp
            if s < m:
                m = s
                r = m * n
    print(r)
