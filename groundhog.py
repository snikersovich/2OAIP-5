def groundhog_day(a):
    for i, (prev, curr) in enumerate(zip(a, a[1:]), 1):
        res = [i for i, (x, y) in enumerate(zip(prev, curr)) if x != y]
        if len(res) > 2:
            return (i,) + tuple(res)
    return 0, 0


data = ['Groundhog Festival in Punxsutawney.',
        'Groundhog Festival in Punksutawney.',
        'Groundhog Festival in Punxsutowney.']
print(groundhog_day(data))
