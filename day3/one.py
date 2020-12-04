with open("input.txt") as file:
    f = file.read().split("\n")
    i = 1
    x = 0
    m = 0
    while f[i]:
        x += 3
        if x < len(f[i]):
            pass
        else:
            x -= len(f[i])
        if f[i][x] == "#":
            m += 1
        print(f[i], f[i][x], m)
        i += 1
    print(m)
