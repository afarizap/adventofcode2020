#!/usr/bin/env python3
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
with open("input.txt") as file:
    f = file.read().split("\n\n")
    n = 0
    for i in f:
        m = 0
        j = i.split(":")
        for last in j:
            if last[-3:] in fields:
                m +=1
        if m > 6:
            n +=1
    print(n)
