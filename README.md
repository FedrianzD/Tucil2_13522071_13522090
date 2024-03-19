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
Program ini adalah program untuk melakukan visualisasi kurva Bezier dengan menggunakan algoritma _midpoint_ yang merupakan implementasi dari algoritma _divide and conquer_. Program memiliki 2 mode, yaitu GUI dan CLI. Baik dalam GUI maupun CLI, pengguna dapat memasukkan sebanyak 3 titik atau n-titik untuk membentuk suatu kurva Bezier.

Untuk membentuk kurva dari titik-titik yang sudah dimasukkan, pengguna perlu memasukkan banyak iterasi untuk membuat kurva Bezier. Semakin besar iterasinya, semakin mulus kurva Bezier yang dihasilkan. Namun seiring meningkatnya iterasi, titik-titik pada kurva juga semakin banyak, sehingga meningkatkan kompleksitas waktu dan ruang yang dibutuhkan.

Selain banyak iterasi dan titik yang membentuk kurva, algoritma yang digunakan juga akan mempengaruhi kompleksitas algoritma program. Dalam tugas ini, digunakan algoritma utama yaitu _Divide and Conquer_ dan algoritma _Bruteforce_ sebagai algoritma pembanding saja.

Pengguna dapat memilih untuk memvisualisasikan kurva secara iteratif dalam bentuk animasi (pada GUI dan CLI) atau hanya menunjukkan kurva hasilnya saja (pada CLI).

## Implementasi Algoritma
Algoritma utama yang digunakan untuk membentuk kurva dari 3 titik dan n-titik input adalah implementasi algoritma _Divide and Conquer_, yaitu algoritma _midpoint_. Langkah-langkah penyelesaian dengan algoritma ini yaitu:
1. Cari titik tengah dari titik kontrol pertama P0 dengan titik kontrol
antara P1 dan beri nama Q1. Cari titik tengah dari titik kontrol antara P1 dengan titik kontrol terakhir P2 dan beri nama Q2. Kemudian cari titik tengah dari Q1 dan Q2 dan beri nama R0. Catat lokasi titik P0, P2, Q1, Q2, dan R0.
2. Masukkan lokasi titik P0 ke dalam larik solusi hanya pada iterasi yang
pertama.
3. Bagi larik yang berisi titik-titik yang telah didapatkan menjadi 2 bagian, yaitu kanan dan kiri. Masing-masing mendapatkan 3 titik dengan titik R0 ada di kedua bagian. Bagian kiri adalah titik P0, titik Q1, dan titik R0. Bagian kanan adalah titik R0, titik Q1, dan titik P2.
4. Lakukan kembali pencarian titik tengah sampai pembagian larik (1-3) menjadi 2 bagian untuk yang bagian kiri jika N > 1 dan dilakukan sebanyak N-1 kali dengan N adalah jumlah iterasi. Pada bagian kiri, titik P0 sebagai titik P0, titik Q1 sebagai titik P1, dan titik R0 sebagai titik P2.
5. Masukkan lokasi titik R0 ke dalam larik solusi.
6. Lakukan kembali pencarian titik tengah sampai membagi larik (1-3) untuk yang bagian kanan jika N > 1 dan dilakukan sebanyak N-1 kali dengan N adalah jumlah iterasi. Pada bagian kiri, titik R0 sebagai titik P0, titik Q2 sebagai titik P1, dan titik P2 sebagai titik P2.
7. Masukkan lokasi titik P2 ke dalam larik solusi hanya pada iterasi yang
pertama.

Sebagai perbandingan kompleksitas, digunakan pula algoritma _Bruteforce_ menggunakan rumus yang sudah disediakan, yaitu:
1. Untuk iterasi sebanyak _i_ kali, bagi kurva menjadi 1 / (2 ^ i)
2. Untuk setiap iterasi, gunakan rumus:
newPoint = ((1-n) ^ 2) x p1 + 2 x (1-n) x n x p2 + (n ^ 2) x p3
3. Masukkan setiap newPoint ke larik solusi
4. Tambahkan titik awal dan titik akhir ke solusi



## Cara Penggunaan
### Requirements
1. Tkinter
2. Custom tkinter (ctk)
3. Matplotlib (matplotlib)

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
program bernilai sangat besar (iterasi di atas 11 atau 12). Hal ini dikarenakan _library_ GUI tidak mampu mengatasi proses yang 
berat dan loading yang berlangsung lama.
5. Jika pengguna menggunakan GUI, pengguna dapat menekan tombol untuk memilih input 3 titik atau n-titik. Input pada n-titik dipisahkan
oleh titik koma (;) untuk setiap titiknya. Contohnya pada input koordinat x sebanyak 5 titik yaitu "1;2;3;4;5" (tanpa tanda kutip).
6. Jika pengguna menggunakan CLI, pengguna akan diminta untuk memasukkan input koordinat x dan y sebanyak 3 titik atau n-titik. Input pada setiap titiknya dipisahkan
oleh spasi untuk koordinat x dan y.

> **_NOTE:_** Jika program mengalami crash saat pengguna menekan tombol submit pada GUI saat generate animasi, masuk ke file GUI.py dan ke fungsi process3Point atau processNPoint, dan ganti fungsi function.animatePlot ke fungsi function.showPlot

> **_NOTE:_** Jika program mengalami crash pada CLI saat pengguna menekan enter untuk generate animasi, cari bagian main dan ganti fungsi function.animatePlot ke fungsi function.showPlot

> **_NOTE:_** Iterasi yang menghasilkan titik solusi mencapai ribuan akan menghasilkan animasi yang sangat lambat jika menggunakan garis bantu iterasi, sehingga animasi akan dinonaktifkan