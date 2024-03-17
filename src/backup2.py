import copy
def mid(point1, point2):
    x = (point1[0] + point2[0])/2
    y = (point1[1] + point2[1])/2
    return (x,y)
def bejir(point1, point2, point3, iterate, iterateMax):
    solution = []
    titikBantu = []
    if iterate == iterateMax:
        pos1 = mid(point1, point2)
        pos2 = mid(point2, point3)
        if iterateMax == 1:
            solution += [point1]
        titikBantu += [pos1]
        solution += [mid(pos1, pos2)]
        titikBantu += [pos2]
        if iterateMax == 1:
            solution += [point3]
        return solution, titikBantu
    elif iterate < iterateMax:
        pos1 = mid(point1, point2)
        pos2 = mid(point2, point3)
        if iterate == 1:
            solution += [point1]
        titikBantu += [[pos1,pos2]]

        temp =  bejir(point1, pos1, mid(pos1,pos2), iterate+1, iterateMax)
        solution += temp[0]
        titikBantu += [temp[1]]

        solution += [mid(pos1, pos2)]

        temp = bejir(mid(pos1,pos2), pos2, point3, iterate+1, iterateMax)
        solution += temp[0]
        titikBantu += [bejir(mid(pos1,pos2), pos2, point3, iterate+1, iterateMax)[1]]
        if iterate == 1:
            solution += [point3]
        return solution, titikBantu    
def bejir2(arr, iterate, iterateMax):
    solution = []
    titikBantu = []
    if iterate == iterateMax:
        tempArr = copy.deepcopy(arr) # buat menampung titik solusi sementara 
        temp = []
        while len(temp) != 1:
            temp = []
            for i in range(len(tempArr)-1):
                temp.append(mid(tempArr[i], tempArr[i+1]))
            tempArr = temp
            titikBantutemp = copy.deepcopy(temp)
            titikBantu.append(titikBantutemp)
        titikBantu = titikBantu[:-1]

        if iterateMax == 1:
            solution += [arr[0]]

        solution += tempArr

        if iterateMax == 1:
            solution += [arr[-1]]

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
                temp.append(mid(arr2[i], arr2[i+1]))
            arrKiri.append(arr2[0])
            arrKanan.append(arr2[-1])
            arr2 = temp
            titikBantutemp = copy.deepcopy(temp)
            titikBantu.append(titikBantutemp)
        titikBantu = titikBantu[:-2]

        # Bagian Kiri
        tempCall = bejir2(arrKiri, iterate+1, iterateMax)
        solution += tempCall[0]
        titikBantu += tempCall[1]

        # Bagian Tengah
        solution += [bejir2(arr, 1, 1)[0][1]]

        # Bagian Kanan
        arrKanan = list(reversed(arrKanan))

        tempCall = bejir2(arrKanan, iterate+1, iterateMax)
        solution += tempCall[0]
        titikBantu += tempCall[1]
        
        # Titik Akhir
        if iterate == 1:
            solution += [arr[-1]]
        return solution, titikBantu
def bejir3(arr, iterate, iterateMax):
    solution = []
    realArr = copy.deepcopy(arr)
    if iterate == iterateMax:
        temp = []
        while len(temp) != 1:
            temp = []
            for i in range(len(realArr)-1):
                temp.append(mid(realArr[i], realArr[i+1]))
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
        solusiTengah = [bejir3(arr, 1, 1)[1]]

        # Bagian Kiri
        arr2 = arr[:-1]
        elementKiri = len(arr2)
        arrKiri = []
        while len(arrKiri) != elementKiri:
            temp = []
            for i in range(len(arr2)-1):
                temp.append(mid(arr2[i], arr2[i+1]))
            arrKiri.append(arr2[0])
            arr2 = temp
        arrKiri += solusiTengah
        solution += bejir3(arrKiri, iterate+1, iterateMax)

        # Bagian Tengah
        solution += solusiTengah

        # Bagian Kanan
        arr3 = arr[1:]
        elementKanan = len(arr3)
        arrKanan = []
        while len(arrKanan) != elementKanan:
            temp = []
            for i in range(len(arr3)-1):
                temp.append(mid(arr3[i], arr3[i+1]))
            arrKanan.append(arr3[-1])
            arr3 = temp
        arrKanan += solusiTengah
        arrKanan = list(reversed(arrKanan))
        solution += bejir3(arrKanan, iterate+1, iterateMax)

        # Titik Akhir
        if iterate == 1:
            solution += [arr[-1]]
        return solution    
def bejirBrute(p1, p2, p3, iterate):
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


