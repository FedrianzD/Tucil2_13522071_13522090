import time
import function
from gui import Gui

def threePointInput():
    try:
        point1 = tuple(map(float, input("Masukkan koordinat titik 1 (x y): ").split()))
        point2 = tuple(map(float, input("Masukkan koordinat titik 2 (x y): ").split()))
        point3 = tuple(map(float, input("Masukkan koordinat titik 3 (x y): ").split()))
        # if point1 == point2 or point2 == point3 or point1 == point3:
        #     raise "Titik tidak boleh sama!"
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
        print("BEZIER CURVE GENERATOR")
        print('1. Masuk lewat GUI\n2. Masuk lewat CLI (jika iterasinya besar)\n3. Keluar')
        choice = int(input("Masukkan pilihan: "))
        if choice == 1:
            App = Gui()
            print("Untuk mengakhiri program, tutup semua window GUI yang berjalan")
            App.mainloop()
            break
        elif choice == 2:
            print('1. Tiga Titik\n2. N Titik')
            choice = int(input("Masukkan pilihan: "))

            if choice == 1:
                point1, point2, point3 = threePointInput()
                iterasi = int(input("Masukkan iterasi: "))
                if iterasi < 1:
                    raise ValueError
                startMid = time.time()
                sol = function.Bezier3Point(point1, point2, point3, 1, iterasi)
                titikBantu = function.Bezier3PointHelper(point1, point2, point3, 1, iterasi)
                endMid = time.time()
                print("Waktu eksekusi algoritma titik tengah: ", endMid - startMid)
                startBrute = time.time()
                sol2 = function.BezierBruteforce(point1, point2, point3, iterasi)
                endBrute = time.time()
                print("Waktu eksekusi algoritma brute force: ", endBrute - startBrute)
                print("Silahkan tutup plot untuk melanjutkan")
                function.animatePlot([point1, point2, point3], sol, titikBantu)
            elif choice == 2:
                arr = nPointInput()
                iterasi = int(input("Masukkan iterasi: "))
                if iterasi < 1:
                    raise ValueError
                startMid = time.time()
                sol = function.BezierNPoint(arr, 1, iterasi)
                endMid = time.time()
                new_array = function.parseArrayNPoint(titikBantu)
                print("Waktu eksekusi algoritma titik tengah: ", endMid - startMid)
                print("Silahkan tutup plot untuk melanjutkan")
                function.animatePlot(arr, sol, new_array)
            else:
                print("\nPilihan tidak valid")
        elif choice == 3:
            break
        print(f'\n')
