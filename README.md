# Program Cek Zodiak & Ramalan (Python)

Program berbasis Python CLI (*Command Line Interface*) sederhana namun cerdas yang berfungsi untuk menentukan Zodiak (Sun Sign) seseorang secara akurat berdasarkan tanggal lahir, serta memberikan "kata-kata mutiara" atau ramalan bulanan yang relevan.

Berbeda dengan program penentuan zodiak biasa yang hanya menggunakan logika `if-else` tanggal (misal: jika tanggal X sampai Y maka Aries), program ini menggunakan **Library Astrologi (Kerykeion)** yang berbasis pada perhitungan astronomi nyata (Swiss Ephemeris) untuk akurasi posisi matahari yang presisi.

---

## Fitur Utama

* **Akurasi Astronomi**: Menggunakan perhitungan derajat matahari yang tepat, bukan sekadar rentang tanggal kalender.
* **Database Ramalan**: Menyediakan pesan motivasi unik untuk ke-12 zodiak.
* **Validasi Input**: Mencegah program *crash* jika pengguna memasukkan huruf pada kolom tanggal/tahun.
* **Auto-Formatting**: Mengonversi output singkatan dari library (misal: "Ari") menjadi nama lengkap ("Aries") agar lebih enak dibaca.

---

## 💻 Prasyarat Sistem

Sebelum menjalankan program ini, pastikan komputer Anda memiliki:

1. **Python 3.x**: Bahasa pemrograman utama.
* Cek dengan mengetik: `python --version` di terminal.


2. **PIP**: Manajer paket untuk menginstal library tambahan.
3. **Koneksi Internet**: Diperlukan hanya saat proses instalasi library.

---

## Instalasi & Penggunaan

### 1. Clone atau Download Repository

Jika file ini ada di GitHub, clone terlebih dahulu. Jika tidak, pastikan file `zodiak.py` ada di folder kerja Anda.

### 2. Install Library Pendukung

Program ini membutuhkan library eksternal bernama `kerykeion`. Buka terminal/CMD dan jalankan perintah:

```bash
pip install kerykeion

```

### 3. Jalankan Program

Ketik perintah berikut di terminal saat berada di dalam folder proyek:

```bash
python zodiak.py

```

*(Atau `python3 zodiak.py` untuk pengguna Linux/Mac)*.

### 4. Cara Pakai

* Masukkan **Nama Lengkap**.
* Masukkan **Tanggal Lahir** (Format angka, misal: 17).
* Masukkan **Bulan Lahir** (Format angka, misal: 8).
* Masukkan **Tahun Lahir** (Format angka, misal: 1945).
* Tekan **Enter** dan lihat hasilnya!

---

## 🔍 Penjelasan Kode Secara Mendalam

Bagian ini akan membedah file `zodiak.py` baris demi baris agar Anda memahami logika di balik layar.

### A. Import Library (Baris 1-2)

```python
import sys
from kerykeion import AstrologicalSubject

```

* **`import sys`**: Modul bawaan Python yang kita gunakan untuk fungsi `sys.exit()`. Ini berguna untuk menghentikan program secara paksa namun rapi jika pengguna melakukan kesalahan input (error handling).
* **`from kerykeion import AstrologicalSubject`**: Kita memanggil kelas `AstrologicalSubject` dari library `kerykeion`. Kelas ini adalah "otak" dari program yang bertugas menghitung posisi planet dan bintang berdasarkan data kelahiran.

### B. Database Kata-Kata (Baris 5-18)

```python
KATA_KATA = {
    "Aries": "Energi bulan ini memanggilmu...",
    "Taurus": "Kesabaran adalah kunci...",
    ...
}

```

* Ini adalah tipe data **Dictionary** (Kamus) dalam Python.
* Formatnya adalah `Key : Value`.
* **Key (Kunci)**: Nama lengkap zodiak (misal "Aries", "Taurus").
* **Value (Nilai)**: Kalimat ramalan atau motivasi yang ingin ditampilkan.
* Data ini bersifat *hardcoded* (tetap), namun bisa dengan mudah diedit atau ditambahkan jika Anda ingin mengubah isi ramalannya.

### C. Fungsi Utama & Input User (Baris 20-31)

```python
def main():
    print("...") # Header UI
    nama_input = input("Masukkan Nama Lengkap : ")
    
    try:
        tgl_lahir = int(input("Tanggal Lahir (1-31)  : "))
        ...
    except ValueError:
        print("\n[!] Error: Harap masukkan angka yang valid.")
        sys.exit()

```

* **`def main():`**: Pembungkus logika utama program agar rapi.
* **`input()`**: Mengambil data dari keyboard pengguna. Data ini awalnya selalu bertipe *String* (teks).
* **`int(...)`**: Kita memaksa (casting) input tanggal, bulan, dan tahun menjadi *Integer* (angka bulat).
* **`try... except ValueError`**: Ini adalah **Error Handling**.
* Jika pengguna iseng memasukkan huruf "abc" saat diminta tanggal, program normal akan *crash*.
* Dengan blok ini, program akan menangkap error tersebut dan memberikan pesan sopan "[!] Error: Harap masukkan angka", lalu keluar (`sys.exit()`) tanpa menampilkan pesan error merah yang menakutkan.



### D. Konfigurasi Lokasi (Baris 34-36)

```python
    lat_fix = -6.2088
    lng_fix = 106.8456
    tz_fix = "Asia/Jakarta"

```

* Dalam astrologi, posisi matahari/zodiak sebenarnya dipengaruhi oleh **Lokasi** dan **Jam** kelahiran.
* Untuk menyederhanakan program agar pengguna tidak pusing mencari koordinat lintang/bujur mereka, program ini menggunakan **Default Jakarta** (Monas).
* Ini adalah asumsi (simplifikasi) agar program lebih ramah pengguna (User Friendly).

### E. Proses Perhitungan Zodiak (Baris 38-44)

```python
    try:
        subjek = AstrologicalSubject(
            nama_input, 
            thn_lahir, bln_lahir, tgl_lahir, 
            12, 00, 
            lat=lat_fix, lng=lng_fix, tz_str=tz_fix,
            city="Jakarta"
        )

```

* Di sini kita membuat **Objek** baru bernama `subjek`.
* Kita memasukkan semua bahan: Nama, Tahun, Bulan, Tanggal, Jam (di-set default jam 12:00 siang), dan Lokasi.
* Saat kode ini berjalan, library `kerykeion` melakukan kalkulasi matematika rumit di latar belakang untuk menentukan posisi matahari pada tanggal tersebut.

### F. Logika Pencocokan String (Baris 46-53)

```python
        zodiak_raw = subjek.sun['sign'] # Output: "Ari", "Tau", "Gem"
        ...
        for key in KATA_KATA:
            if key.startswith(zodiak_raw): 
                pesan_bulanan = KATA_KATA[key]
                zodiak_display = key 
                break

```

* **Masalah**: Library `kerykeion` secara default mengembalikan nama zodiak yang disingkat 3 huruf (misal: "Ari", "Leo", "Sco"). Sedangkan database kita menggunakan nama lengkap ("Aries", "Leo", "Scorpio").
* **Solusi**: Kita melakukan *looping* (perulangan) untuk mengecek database `KATA_KATA`.
* **`key.startswith(zodiak_raw)`**: Logika cerdas ini mengecek: "Apakah kata 'Scorpio' diawali dengan 'Sco'?". Jika **Ya (True)**, maka kita ambil ramalannya, dan kita ubah tampilan namanya menjadi nama lengkap ("Scorpio") agar lebih bagus saat diprint.

### G. Menampilkan Output (Baris 56-62)

```python
        print(f"Nama          : {subjek.name}")
        ...
        print(f"Zodiak Kamu   : {zodiak_display}") 
        print(f"Kata-kata     : \"{pesan_bulanan}\"")

```

* Menggunakan **f-string** (format string) Python untuk menggabungkan teks dan variabel dengan rapi.
* Variabel `zodiak_display` yang diprint adalah versi nama lengkap yang sudah diproses di tahap sebelumnya.

### H. Eksekusi Program (Baris 66-67)

```python
if __name__ == "__main__":
    main()

```

* Ini adalah standar *best practice* Python.
* Kode ini memastikan bahwa fungsi `main()` hanya akan dijalankan jika file ini dibuka langsung oleh pengguna. Jika file ini di-import oleh file lain sebagai modul, kode tidak akan jalan otomatis.

### I. Kode Komentar (Baris 71+)

Di bagian bawah file terdapat kode yang dikomentari (*commented out*). Kode tersebut adalah sisa eksperimen (boilerplate) untuk fitur lanjutan: **Membuat Grafik Natal Chart (SVG)**. Fitur ini dinonaktifkan sementara agar program tetap ringan dan fokus pada output teks saja.

---

## 🛠️ Kemungkinan Error (Troubleshooting)

1. **ModuleNotFoundError: No module named 'kerykeion'**
* *Penyebab*: Anda belum menginstal library.
* *Solusi*: Jalankan `pip install kerykeion`.


2. **Output Zodiak Salah?**
* *Penyebab*: Jam lahir di-set default ke 12:00 siang.
* *Penjelasan*: Zodiak berpindah posisi setiap sekitar tanggal 20-23. Jika Anda lahir tepat di tanggal perbatasan (cusp), jam lahir sangat berpengaruh. Karena jam di-hardcode, ada kemungkinan margin error kecil bagi mereka yang lahir di tanggal pergantian zodiak.



---

## 👨‍💻 Author

Dibuat sebagai proyek latihan Algoritma & Pemrograman Python.

* **Coder**: 
- Maharani 
- Zahra
- Pedro
- ilfan

* **Tahun**: 2026
