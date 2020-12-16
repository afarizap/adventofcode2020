#!/usr/bin/env python3

with open("input") as test:
    f = test.read().split()
    seats = {}
    seat_id = 1
    height = len(f) + 2
    width = len(f[0]) + 2
    moves = [-width - 1, -width, -width + 1,
             -1, 1,
             width - 1, width, width + 1]
    """ creating dict """
    for _ in range(width):
        seats[seat_id] = '1'
        seat_id += 1
    for row in f:
        seats[seat_id] = '1'
        seat_id += 1
        for seat in row:
            seats[seat_id] = seat
            seat_id += 1
        seats[seat_id] = '1'
        seat_id += 1
    for _ in range(width):
        seats[seat_id] = '1'
        seat_id += 1
    """ first row """
    for key, val in seats.items():
        if val == 'L':
            seats.update({key: '#'})
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
    """ second row """
    new = seats.copy()
    for key, val in seats.items():
        temp = 0
        if val == '#':
            for _ in moves:
                if seats[key + _] == '#':
                    temp += 1
            if temp >= 4:
                new.update({key: 'L'})
        if val == 'L':
            for _ in moves:
                if seats[key + _] == '#':
                    temp +=1
            if temp == 0:
                new.update({key: '#'})
    seats = new
    """ list format """
    asd = []
    for _ in seats.values():
        asd.append(_)
    """ count seats occupied """
    count = 0
    for key, val in seats.items():
        if val == '#':
            count += 1
    print(count)
