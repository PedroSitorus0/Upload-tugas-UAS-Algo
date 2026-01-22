from kerykeion import AstrologicalSubject
from datetime import datetime # Kita butuh ini untuk ambil waktu sekarang
import zodiak

def main():
    print("--- INFO LANGIT JAKARTA SAAT INI (REAL-TIME) ---\n")
    
    # 1. Konfigurasi Lokasi
    latitude = -6.2088
    longitude = 106.8456
    timezone = "Asia/Jakarta" 

    # 2. Ambil Waktu Sekarang (Otomatis)
    # Ini diperlukan karena AstrologicalSubject TIDAK BISA kosong
    sekarang = datetime.now()

    try:
        # Masukkan waktu sekarang ke dalam subjek
        subjek = AstrologicalSubject(
            "Langit Saat Ini",  # Nama Dummy
            sekarang.year,      # Tahun sekarang
            sekarang.month,     # Bulan sekarang
            sekarang.day,       # Hari sekarang
            sekarang.hour,      # Jam sekarang
            sekarang.minute,    # Menit sekarang
            lat=latitude,
            lng=longitude,
            tz_str=timezone,
            city="Jakarta",
            nation="ID"
        )

        # Mengambil data planet saat ini
        sun_sign = subjek.sun['sign']
        moon_sign = subjek.moon['sign']
        ascendant = subjek.first_house['sign'] # Ascendant butuh jam akurat

        print(f"Waktu Cek     : {sekarang.strftime('%Y-%m-%d %H:%M')}")
        print(f"Lokasi        : Jakarta (Lat: {latitude}, Lng: {longitude})")
        print("-" * 40)
        print(f"Matahari (Sun): {sun_sign}")
        print(f"Bulan (Moon)  : {moon_sign}")
        print(f"Ascendant     : {ascendant}")
        print(f"Derajat Sun   : {subjek.sun['abs_pos']:.2f}°")
        print("-" * 40 + "\n")

    except Exception as e:
        print(f"Masih terjadi kesalahan: {e}")

    # 3. Panggil Program Interaktif (Input Manual)
    # Katup dibuka di sini
    print(">>> Masuk ke Menu Cek Zodiak Personal...")
    zodiak.main()

if __name__ == "__main__":
    main()