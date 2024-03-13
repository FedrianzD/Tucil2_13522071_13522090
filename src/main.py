import matplotlib.pyplot as plt

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

if __name__ == "__main__":
    point1 = (1,0)
    point2 = (3,4)
    point3 = (5,0)
    sol = []
    sol = bejir(point1, point2, point3, 1, 3)
    print(sol)
    plt.plot([point[0] for point in sol], [point[1] for point in sol], 'ro-')
    plt.plot([point[0] for point in sol], [point[1] for point in sol], 'b-', label='Kurva Graf Bezier dengan Algoritma Titik Tengah')
    plt.plot(point1[0], point1[1], 'go')
    plt.plot(point2[0], point2[1], 'go')
    plt.plot(point3[0], point3[1], 'go')
    plt.plot([1, 3], [0, 4], 'r-')
    plt.plot([3, 5], [4, 0], 'r')
    plt.title('Kurva Graf Bezier dengan Algoritma Titik Tengah')
    plt.legend()
    plt.show()