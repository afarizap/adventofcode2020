with open("input.txt") as file:
    f = file.read().split("\n")
    i = 2
    j = 0
    m = 0
    x = 1
    y = 2
    while f[i-1]:
        j += x
        if j < len(f[i]):
            pass
        else:
            j -= len(f[i])
        if f[i][j] == "#":
            m += 1
        i += y
    print(m)
