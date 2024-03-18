# Tucil 2
## Implementasi Algoritma Divide and Conquer pada Pembuatan Kurva Bezier Berbasis Algoritma Titik Tengah

| No. | Nama                     |   NIM    |
|:---:|:-------------------------|:--------:|
| 1.  | Bagas Sambega Rosyada    | 13522071 |
| 2.  | Fedrianz Dharma          | 13522090 |

## Daftar Isi
1. [Deskripsi Tugas](#deskripis-tugas)
2. [Implementasi Algoritma](#implementasi)
3. [Cara Penggunaan](#cara-penggunaan)

## Deskripsi Tugas

## Implementasi Algoritma

## Cara Penggunaan
### Requirements
1. Tkinter
2. Custom tkinter (ctk)
3. Matplotlib (matplotlib)
4. 

### Cara Install
```bash
pip install tk
pip install ctk
pip install matplotlib
```
Jika modul tkinter tidak ditemukan (Linux), maka install dengan menggunakan
```
sudo apt-get install python3-tk
```

### Cara Menjalankan Program
1. Buka terminal
2. Masuk ke direktori src
3. Jalankan perintah berikut
```bash
python main.py
```
atau
```
python3 main.py
```
4. Program akan berjalan dan memberikan opsi pada pengguna untuk menggunakan
GUI atau CLI. Program disarankan menggunakan CLI jika iterasi yang akan digunakan pada
program bernilai sangat besar. Hal ini dikarenakan _library_ GUI tidak mampu mengatasi proses yang 
berat dan loading yang berlangsung lama.
5. Jika pengguna menggunakan GUI, pengguna dapat menekan tombol untuk memilih input 3 titik atau n-titik. Input pada n-titik dipisahkan
oleh titik koma (;) untuk setiap titiknya. Contohnya pada input koordinat x sebanyak 5 titik yaitu "1;2;3;4;5" (tanpa tanda kutip).
6. Jika pengguna menggunakan CLI, pengguna akan diminta untuk memasukkan input koordinat x dan y sebanyak 3 titik atau n-titik. Input pada setiap titiknya dipisahkan
oleh spasi untuk koordinat x dan y.

> **_NOTE:_** Jika program mengalami crash saat pengguna menekan tombol submit pada GUI saat generate animasi, masuk ke file GUI.py dan ke fungsi process3Point atau processNPoint, dan ganti fungsi function.animatePlot ke fungsi function.showPlot

> **_NOTE:_** Jika program mengalami crash pada CLI saat pengguna menekan enter untuk generate animasi, cari bagian main dan ganti fungsi function.animatePlot ke fungsi function.showPlot