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
    
def bejir2(arr, iterate, iterateMax):
    solution = []
    if iterate == iterateMax:
        temp = []
        while len(temp) != 1:
            temp = []
            for i in range(len(arr)-1):
                temp.append(mid(arr[i], arr[i+1]))
            arr = temp
        solution += arr
        return solution
    elif iterate < iterateMax:

        # Titik Awal
        if iterate == 1:
            solution += [arr[0]]
        solusiTengah = bejir2(arr, 1, 1)

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
        solution += bejir2(arrKiri, iterate+1, iterateMax)

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
        solution += bejir2(arrKanan, iterate+1, iterateMax)
        
        # Titik Akhir
        if iterate == 1:
            solution += [arr[-1]]
        return solution
        
point1 = (1,0)
point2 = (3,3)
point3 = (5,3)
point4 = (5,0)
point5 = (5,5)
arr = [point1,point2,point3,point4, point5]
sol = []
sol = bejir(point1, point2, point3, 1, 4)
sol2 = bejir2(arr, 1, 3)
print(sol2)