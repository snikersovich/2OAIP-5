def gears(data, n, m):
    ratio = n/m
    for box in data:
        for x in box:
            if x == 0:
                continue
            s = x * ratio
            if s in box:
                return int(s), x
    return None, None

data = [[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]]
print(gears(data, 30, 7))