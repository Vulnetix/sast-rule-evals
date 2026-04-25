def complex_func(x, y, z):
    if x > 0:
        if y > 0:
            if z > 0:
                return 1
            elif z < 0:
                return 2
            else:
                return 3
        elif y < 0:
            if z > 0:
                return 4
            elif z < 0:
                return 5
            else:
                return 6
        else:
            if z > 0:
                return 7
            elif z < 0:
                return 8
            else:
                return 9
    elif x < 0:
        if y > 0:
            return 10
        elif y < 0:
            return 11
    return 0
