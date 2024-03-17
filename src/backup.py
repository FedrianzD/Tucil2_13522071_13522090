# def bejir2(arr, iterate, iterateMax):
#     solution = []
#     titikBantu = []
#     tempArr = copy.deepcopy(arr) # buat menampung titik solusi sementara 
#     if iterate == iterateMax:
        
#         temp = []
#         while len(temp) != 1:
#             temp = []
#             for i in range(len(tempArr)-1):
#                 temp.append(mid(tempArr[i], tempArr[i+1]))
#             tempArr = temp
#             titikBantutemp = copy.deepcopy(temp)
#             titikBantu.append(titikBantutemp)
#         titikBantu = titikBantu[:-1]

#         if iterateMax == 1:
#             solution += [arr[0]]

#         solution += tempArr

#         if iterateMax == 1:
#             solution += [arr[-1]]

#         return solution, titikBantu
#     elif iterate < iterateMax:

#         # Titik Awal
#         if iterate == 1:
#             solution += [arr[0]]
#         # solusiTengah = [bejir2(arr, 1, 1)[0][1]]

#         # Bagian Kiri
#         arr2 = arr
#         elementKiri = len(arr2)
#         arrKiri = []
#         while len(arrKiri) != elementKiri:
#             temp = []
#             for i in range(len(arr2)-1):
#                 temp.append(mid(arr2[i], arr2[i+1]))
#             arrKiri.append(arr2[0])
#             arr2 = temp
#             titikBantutemp = copy.deepcopy(temp)
#             titikBantu.append(titikBantutemp)
#         titikBantu = titikBantu[:-2]
#         # arrKiri += solusiTengah

#         tempCall = bejir2(arrKiri, iterate+1, iterateMax)
#         solution += tempCall[0]
#         titikBantu += tempCall[1]

#         # Bagian Tengah
#         solution += [bejir2(arr, 1, 1)[0][1]]

#         # Bagian Kanan
#         arr3 = arr
#         elementKanan = len(arr3)
#         arrKanan = []
#         while len(arrKanan) != elementKanan:
#             temp = []
#             for i in range(len(arr3)-1):
#                 temp.append(mid(arr3[i], arr3[i+1]))
#             arrKanan.append(arr3[-1])
#             arr3 = temp
#             titikBantutemp = copy.deepcopy(temp)
#             titikBantu.append(titikBantutemp)
#         titikBantu = titikBantu[:-2]
#         # arrKanan += solusiTengah
#         arrKanan = list(reversed(arrKanan))

#         tempCall = bejir2(arrKanan, iterate+1, iterateMax)
#         solution += tempCall[0]
#         titikBantu += tempCall[1]
        
#         # Titik Akhir
#         if iterate == 1:
#             solution += [arr[-1]]
#         return solution, titikBantu


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
    return count