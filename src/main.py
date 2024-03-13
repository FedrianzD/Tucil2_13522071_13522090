def mid(point1, point2):
    x = (point1[0] + point2[0])/2
    y = (point1[1] + point2[1])/2
    return (x,y)
def bejir(point1, point2, point3, iterate, iterateMax):
    solution = []
    if iterate == iterateMax:
        pos1 = mid(point1, point2)
        pos2 = mid(point2, point3)
        solution += [mid(pos1, pos2)]
        return solution
    elif iterate < iterateMax:
        pos1 = mid(point1, point2)
        pos2 = mid(point2, point3)
        if iterate == 1:
            solution += [point1]
        solution += bejir(point1, pos1, mid(pos1,pos2), iterate+1, iterateMax)
        solution += [mid(pos1, pos2)]
        solution += bejir(mid(pos1,pos2), pos2, point3, iterate+1, iterateMax)
        if iterate == 1:
            solution += [point3]
        return solution
point1 = (1,0)
point2 = (3,4)
point3 = (5,0)
sol = []
sol = bejir(point1, point2, point3, 1, 3)
print(sol)