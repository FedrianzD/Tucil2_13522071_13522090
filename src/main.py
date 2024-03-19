import time
import function
from gui import Gui

def threePointInput():
    arr = []
    for i in range(3):
        while True:
            try:
                temp = (tuple(map(float, input(f"Masukkan koordinat titik {i+1} (x y): ").split())))
                if len(temp) != 2:
                    print("Koordinat harus terdiri dari 2 nilai!")
                else:
                    arr.append(temp)
                    break
            except ValueError:
                print("Input harus berupa angka!")
    return arr[0], arr[1], arr[2]


def nPointInput():
    while True:
        try:
            n = int(input("Masukkan jumlah titik: "))
            if n <= 2:
                print("Minimal 3 titik!")
                continue
            else:
                break
        except ValueError:
            print("Input harus berupa integer!")
    arr = []
    for i in range(n):
        while True:
            try:
                temp = (tuple(map(float, input(f"Masukkan koordinat titik {i+1} (x y): ").split())))
                if len(temp) != 2:
                    print("Koordinat harus terdiri dari 2 nilai!")
                else:
                    arr.append(temp)
                    break
            except ValueError:
                print("Input harus berupa angka!")
    return arr
    


if __name__ == "__main__":
    while True:
        print("BEZIER CURVE GENERATOR")
        print('1. Masuk lewat GUI\n2. Masuk lewat CLI (jika iterasinya besar)\n3. Keluar')
        try:
            choice = int(input("Masukkan pilihan: "))
        except ValueError:
            print("Input harus berupa integer!\n")
            continue
        
        if choice == 1:
            App = Gui()
            print("Untuk mengakhiri program, tutup semua window GUI yang berjalan")
            App.mainloop()
            break
        
        elif choice == 2:
            print('1. Tiga Titik\n2. N Titik')
            while True:
                try:
                    choice = int(input("Masukkan pilihan: "))
                except ValueError:
                    print("Input harus berupa integer!")
                    continue
                if choice == 1 or choice == 2:
                    break
                else:
                    print('Pilihan tidak tersedia! Silahkan masukkan ulang (1/2)')
                    continue
                
            if choice == 1:
                point1, point2, point3 = threePointInput()
                while True:
                    try:
                        iterasi = int(input("Masukkan iterasi: "))
                        if iterasi < 1:
                            print("Iterasi minimal 1 kali!")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Input harus berupa integer!")
                        continue
                startBrute = time.perf_counter()
                sol2 = function.BezierBruteforce(point1, point2, point3, iterasi)
                endBrute = time.perf_counter()
                print("Waktu eksekusi algoritma brute force: ", (endBrute - startBrute) * 1000)
                startMid = time.perf_counter()
                sol = function.Bezier3Point(point1, point2, point3, 1, iterasi)
                endMid = time.perf_counter()
                titikBantu = function.Bezier3PointHelper(point1, point2, point3, 1, iterasi)
                print("Waktu eksekusi algoritma titik tengah: ", (endMid - startMid) * 1000)
                if iterasi == 1:
                    titikBantu = function.parseArrayNPoint(titikBantu)
                print("Silahkan tutup plot untuk melanjutkan")
                function.animatePlot([point1, point2, point3], sol, titikBantu)
                # function.showPlot([point1, point2, point3], sol, titikBantu)
            
            elif choice == 2:
                arr = nPointInput()
                while True:
                    try:
                        iterasi = int(input("Masukkan iterasi: "))
                        if iterasi < 1:
                            print("Iterasi minimal 1 kali!")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Input harus berupa integer!")
                        continue
                startMid = time.time()
                temp = function.BezierNPoint(arr, 1, iterasi)
                sol = temp[0]
                titikBantu = temp[1]
                endMid = time.time()
                new_array = function.parseArrayNPoint(titikBantu)
                print("Waktu eksekusi algoritma titik tengah: ", (endMid - startMid) * 1000)
                print("Silahkan tutup plot untuk melanjutkan")
                function.animatePlot(arr, sol, new_array)
                # function.showPlot(arr, sol, new_array)
            else:
                print("\nPilihan tidak valid")
                
        elif choice == 3:
            break
        else:
            print("Pilihan tidak tersedia!\n")
            continue
        print('\n')
