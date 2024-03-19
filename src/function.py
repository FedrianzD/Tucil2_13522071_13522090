import copy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def DnC(point1, point2):
    x = (point1[0] + point2[0])/2
    y = (point1[1] + point2[1])/2
    return (x,y)

# 3 titik
def Bezier3Point(point1, point2, point3, iterate, iterateMax):
    solution = []
    # titikBantu = []
    if iterate == iterateMax:
        pos1 = DnC(point1, point2)
        pos2 = DnC(point2, point3)

        if iterateMax == 1:
            solution.append(point1)
        #     titikBantu.append([point1])
        # titikBantu.append([pos1, pos2])

        solution.append(DnC(pos1, pos2))

        if iterateMax == 1:
            solution.append(point3)
            # titikBantu.append([point3])

        return solution

    elif iterate < iterateMax:
        pos1 = DnC(point1, point2)
        pos2 = DnC(point2, point3)

        if iterate == 1:
            solution.append(point1)

        # titikBantu.append([pos1, pos2])

        temp = Bezier3Point(point1, pos1, DnC(pos1, pos2), iterate + 1, iterateMax)
        solution += temp
        # titikBantu += temp[1]

        solution.append(DnC(pos1, pos2))

        temp = Bezier3Point(DnC(pos1, pos2), pos2, point3, iterate + 1, iterateMax)
        solution += temp
        # titikBantu += temp[1]

        if iterate == 1:
            solution.append(point3)

        return solution
    

def Bezier3PointHelper(point1, point2, point3, iterate, iterateMax):
    # solution = []
    titikBantu = []
    if iterate == iterateMax:
        pos1 = DnC(point1, point2)
        pos2 = DnC(point2, point3)

        if iterateMax == 1:
            # solution.append(point1)
            titikBantu.append([point1])
        titikBantu.append([pos1, pos2])

        # solution.append(DnC(pos1, pos2))

        if iterateMax == 1:
            # solution.append(point3)
            titikBantu.append([point3])

        return titikBantu

    elif iterate < iterateMax:
        pos1 = DnC(point1, point2)
        pos2 = DnC(point2, point3)

        # if iterate == 1:
        #     solution.append(point1)

        titikBantu.append([pos1, pos2])

        temp = Bezier3PointHelper(point1, pos1, DnC(pos1, pos2), iterate + 1, iterateMax)
        # solution += temp[0]
        titikBantu += temp

        # solution.append(DnC(pos1, pos2))

        temp = Bezier3PointHelper(DnC(pos1, pos2), pos2, point3, iterate + 1, iterateMax)
        # solution += temp[0]
        titikBantu += temp

        # if iterate == 1:
        #     solution.append(point3)

        return titikBantu


# n titik
def BezierNPoint(arr, iterate, iterateMax):
    solution = []
    titikBantu = []
    if iterate == iterateMax:
        tempArr = copy.deepcopy(arr) # buat menampung titik solusi sementara 
        temp = []
        while len(temp) != 1:
            temp = []
            for i in range(len(tempArr)-1):
                temp.append(DnC(tempArr[i], tempArr[i+1]))
            tempArr = temp
            titikBantutemp = copy.deepcopy(temp)
            titikBantu.append(titikBantutemp)
        titikBantu = titikBantu[:-1]

        if iterateMax == 1:
            solution += [arr[0]]
            titikBantu.append(arr[0])

        solution += tempArr

        if iterateMax == 1:
            solution += [arr[-1]]
            titikBantu.append(arr[0])

        return solution, titikBantu
    elif iterate < iterateMax:

        # Titik Awal
        if iterate == 1:
            solution += [arr[0]]

        # Tahap Awal
        arr2 = arr
        arrKiri = []
        arrKanan = []
        while len(arrKiri) != len(arr):
            temp = []
            for i in range(len(arr2)-1):
                temp.append(DnC(arr2[i], arr2[i+1]))
            arrKiri.append(arr2[0])
            arrKanan.append(arr2[-1])
            arr2 = temp
            titikBantutemp = copy.deepcopy(temp)
            titikBantu.append(titikBantutemp)
        titikBantu = titikBantu[:-2]

        # Bagian Kiri
        tempCall = BezierNPoint(arrKiri, iterate+1, iterateMax)
        solution += tempCall[0]
        titikBantu += tempCall[1]

        # Bagian Tengah
        solution += [BezierNPoint(arr, 1, 1)[0][1]]

        # Bagian Kanan
        arrKanan = list(reversed(arrKanan))

        tempCall = BezierNPoint(arrKanan, iterate+1, iterateMax)
        solution += tempCall[0]
        titikBantu += tempCall[1]
        
        # Titik Akhir
        if iterate == 1:
            solution += [arr[-1]]
        return solution, titikBantu



def BezierBackup(arr, iterate, iterateMax):
    solution = []
    realArr = copy.deepcopy(arr)
    if iterate == iterateMax:
        temp = []
        while len(temp) != 1:
            temp = []
            for i in range(len(realArr)-1):
                temp.append(DnC(realArr[i], realArr[i+1]))
            realArr = temp
        if iterateMax == 1:
            solution += [arr[0]]
        solution += realArr
        if iterateMax == 1:
            solution += [arr[-1]]
        return solution
    elif iterate < iterateMax:

        # Titik Awal
        if iterate == 1:
            solution += [arr[0]]
        solusiTengah = [BezierBackup(arr, 1, 1)[1]]

        # Bagian Kiri
        arr2 = arr[:-1]
        elementKiri = len(arr2)
        arrKiri = []
        while len(arrKiri) != elementKiri:
            temp = []
            for i in range(len(arr2)-1):
                temp.append(DnC(arr2[i], arr2[i+1]))
            arrKiri.append(arr2[0])
            arr2 = temp
        arrKiri += solusiTengah
        solution += BezierBackup(arrKiri, iterate+1, iterateMax)

        # Bagian Tengah
        solution += solusiTengah

        # Bagian Kanan
        arr3 = arr[1:]
        elementKanan = len(arr3)
        arrKanan = []
        while len(arrKanan) != elementKanan:
            temp = []
            for i in range(len(arr3)-1):
                temp.append(DnC(arr3[i], arr3[i+1]))
            arrKanan.append(arr3[-1])
            arr3 = temp
        arrKanan += solusiTengah
        arrKanan = list(reversed(arrKanan))
        solution += BezierBackup(arrKanan, iterate+1, iterateMax)

        # Titik Akhir
        if iterate == 1:
            solution += [arr[-1]]
        return solution    

def BezierBruteforce(p1, p2, p3, iterate):
    npoint = 2**iterate + 1
    temp = 1/ (npoint-1)
    n = temp
    solution = []
    solution += [p1]
    count = 0
    while n <= (1-temp):
        rx = ((1-n)**2)*p1[0] + 2*(1-n)*n*p2[0] + (n**2)*p3[0]
        ry = ((1-n)**2)*p1[1] + 2*(1-n)*n*p2[1] + (n**2)*p3[1]
        solution += [(rx,ry)]
        n += temp
        count+=1
    solution += [p3]
    return solution


def showPlot(arrayOfPoints, arrayOfSol, arrayOfHelper):
    plt.close()
    # show helper
    for arr in arrayOfHelper:
        plt.plot([point[0] for point in arr], [point[1] for point in arr],  linestyle='dotted', color='green')

    # Show main bezier plot result
    plt.plot([point[0] for point in arrayOfSol], [point[1] for point in arrayOfSol], 'ro', markersize=2 if len(arrayOfSol) > 30 else 3)
    plt.plot([point[0] for point in arrayOfSol], [point[1] for point in arrayOfSol], 'b-', label='Kurva Graf Bezier dengan Algoritma Titik Tengah')
    plt.plot([point[0] for point in arrayOfPoints], [point[1] for point in arrayOfPoints], 'go')
    plt.plot([point[0] for point in arrayOfPoints], [point[1] for point in arrayOfPoints], 'r-')
    plt.legend()
    plt.grid()
    plt.show()

def animatePlot(arrayOfPoints, arrayOfSol, arrayOfHelper):
    plt.close()
    fig, ax = plt.subplots()
    linePoints, = ax.plot([], [], 'ro-')
    lineSol, = ax.plot([], [], 'bo-', markersize=2 if len(arrayOfSol) > 30 else 3)
    lineHelper, = ax.plot([], [], linestyle='dotted', color='green')

    ax.set_xlim(min([point[0] for point in arrayOfPoints]) - 1, max([point[0] for point in arrayOfPoints]) + 1)
    ax.set_ylim(min([point[1] for point in arrayOfPoints]) - 1, max([point[1] for point in arrayOfPoints]) + 1)
    currentPointsX = []
    currentPointsY = []
    currentSolX = []
    currentSolY = []
    currentHelperX = []
    currentHelperY = []
    currentIteration = 0
    def animate(i):
        if i < len(arrayOfSol):
            currentSolX.append(arrayOfSol[i][0])
            currentSolY.append(arrayOfSol[i][1])
            lineSol.set_data(currentSolX, currentSolY)
        if i < len(arrayOfPoints):
            currentPointsX.append(arrayOfPoints[i][0])
            currentPointsY.append(arrayOfPoints[i][1])
            linePoints.set_data(currentPointsX, currentPointsY)
        if i < len(arrayOfHelper):
            currentHelperX.append([point[0] for point in arrayOfHelper[i]])
            currentHelperY.append([point[1] for point in arrayOfHelper[i]])
            lineHelper.set_data(currentHelperX, currentHelperY)
    
    if len(arrayOfHelper) < 100:
        interval = 200
    elif 100 <= len(arrayOfHelper) < 800:
        interval = 50
    else:
        interval = 2
    ani = FuncAnimation(fig, animate, frames=max(len(arrayOfSol), len(arrayOfHelper), len(arrayOfPoints)), interval=interval , repeat=False)
    plt.grid()
    plt.show()
    
    
def parseArrayNPoint(titikBantu):
    temp = []
    for array in titikBantu:
        for subarray in array:
            temp.append(subarray)
    
    new = []
    res = []
    for point in temp:
        if len(new) != 2:
            new.append(point)
        else:
            res.append(new)
    return res
        # new_array = []
    # for subarray in titikBantu:
    #     if len(subarray) >= 2:
    #         new_subarray = subarray[:2]
    #     else:
    #         new_subarray = subarray + [None] * (2 - len(subarray))
    #     new_array.append(new_subarray)
    
    # return new_array