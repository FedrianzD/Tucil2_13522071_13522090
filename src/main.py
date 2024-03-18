import time

import matplotlib.pyplot as plt
import function
from gui import Gui

def threePointInput():
    try:
        point1 = tuple(map(float, input("Masukkan koordinat titik 1 (x y): ").split()))
        point2 = tuple(map(float, input("Masukkan koordinat titik 2 (x y): ").split()))
        point3 = tuple(map(float, input("Masukkan koordinat titik 3 (x y): ").split()))
        if point1 == point2 or point2 == point3 or point1 == point3:
            raise "Titik tidak boleh sama!"
        return point1, point2, point3
    except:
        print("Input tidak valid")


def nPointInput():
    try:
        n = int(input("Masukkan jumlah titik: "))
        arr = []
        for i in range(n):
            arr.append(tuple(map(float, input(f"Masukkan koordinat titik {i+1} (x y): ").split())))
        return arr
    except:
        print("Input tidak valid")


if __name__ == "__main__":
    while True:
        print(f'1. Masuk lewat GUI\n2. Masuk lewat CLI (jika iterasinya besar)\n3. Keluar')
        try:
            choice = int(input("Masukkan pilihan: "))
            if choice == 1:
                App = Gui()
                App.mainloop()
                break
            elif choice == 2:
                print(f'1. Tiga Titik\n2. N Titik')
                choice = int(input("Masukkan pilihan: "))

                if choice == 1:
                    point1, point2, point3 = threePointInput()
                    iterasi = int(input("Masukkan iterasi: "))
                    if iterasi < 1:
                        raise ValueError
                    startMid = time.time()
                    sol, titikBantu = function.Bezier3Point(point1, point2, point3, 1, iterasi)
                    endMid = time.time()
                    print("Waktu eksekusi algoritma titik tengah: ", endMid - startMid)
                    startBrute = time.time()
                    sol2 = function.BezierBruteforce(point1, point2, point3, iterasi)
                    endBrute = time.time()
                    print("Waktu eksekusi algoritma brute force: ", endBrute - startBrute)
                    print("Silahkan tutup plot untuk melanjutkan")
                    function.showPlot([point1, point2, point3], sol, titikBantu)
                elif choice == 2:
                    arr = nPointInput()
                    iterasi = int(input("Masukkan iterasi:"))
                    if iterasi < 1:
                        raise ValueError
                    startMid = time.time()
                    sol, titikBantu = function.BezierNPoint(arr, 1, iterasi)
                    endMid = time.time()
                    print("Waktu eksekusi algoritma titik tengah: ", endMid - startMid)
                    print("Silahkan tutup plot untuk melanjutkan")
                    function.showPlot(arr, sol, titikBantu)
                else:
                    print("\nPilihan tidak valid")
            elif choice == 3:
                break
        except:
            print("Input tidak valid")
        print(f'\n')


# point1 = (0,0)
# point2 = (3,3)
# point3 = (6,0)
# point4 = (5,0)
# point5 = (5,10)
# arr = [point1,point2,point3,point4, point5]
# # jaw = function.bejir(point1, point2, point3, 1, 2)
# # print(len(sol))
# # sol2 = function.bejirBrute(point1, point2, point3, 1)
# sol2 = function.bejir2(arr, 1, 2)
# sol3 = function.bejir3(arr, 1, 2)
# # print(jaw[0])
# # print(jaw[1])
# print(sol2[0])
# print()
# print(sol2[1])
# print()
# print(sol3)
# print(function.mid((4,1.125), (5.125,1)))

# point1 = (1,0)
# point2 = (3,4)
# point3 = (5,0)
# sol, titikBantu = function.Bezier3Point(point1, point2, point3, 1, 20)
# print(len(titikBantu))
# print(sol)
# for arr in titikBantu:
#     print(len(arr), arr)
# for helper_set in titikBantu:
#         if isinstance(helper_set[0], list):  # multiple helper points
#             for helper_points in helper_set:
#                 points_x = [point[0] for point in helper_points]
#                 points_y = [point[1] for point in helper_points]
#                 plt.plot(points_x, points_y, linestyle='dotted', color='green')
#         else:  # single helper point
#             points_x = [point[0] for point in helper_set]
#             points_y = [point[1] for point in helper_set]
#             plt.plot(points_x, points_y, linestyle='dotted', color='green')
# plt.plot([point[0] for point in sol], [point[1] for point in sol], 'ro')
# plt.plot([point[0] for point in sol], [point[1] for point in sol], 'b-', label='Kurva Graf Bezier dengan Algoritma Titik Tengah')
# plt.plot(point1[0], point1[1], 'go')
# plt.plot(point2[0], point2[1], 'go')
# plt.plot(point3[0], point3[1], 'go')
# plt.plot([1, 3], [0, 4], 'r-')
# plt.plot([3, 5], [4, 0], 'r')
# plt.title('Kurva Graf Bezier dengan Algoritma Titik Tengah')
# plt.legend()
# plt.show()