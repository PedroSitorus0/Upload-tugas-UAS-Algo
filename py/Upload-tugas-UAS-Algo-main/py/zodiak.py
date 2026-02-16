import sys
from kerykeion import AstrologicalSubject

# Database Kata-kata (Tetap Nama Lengkap agar rapi saat diprint)
KATA_KATA = {
    "Aries": "Energi bulan ini memanggilmu untuk memulai petualangan baru. Jangan ragu mengambil risiko terukur.",
    "Taurus": "Kesabaran adalah kunci. Fokus pada stabilitas keuangan dan nikmati prosesnya.",
    "Gemini": "Komunikasimu sedang sangat baik. Waktu yang tepat untuk memperluas jaringan atau belajar skill baru.",
    "Cancer": "Dengarkan intuisimu. Berikan perhatian lebih pada keluarga dan kenyamanan rumah.",
    "Leo": "Saatnya bersinar! Kreativitasmu sedang di puncaknya, jangan takut tampil beda.",
    "Virgo": "Detail kecil sangat penting bulan ini. Rapikan rencanamu untuk hasil yang sempurna.",
    "Libra": "Carilah keseimbangan antara kerja dan istirahat. Harmoni adalah prioritasmu.",
    "Scorpio": "Transformasi sedang terjadi. Lepaskan apa yang tidak lagi berguna bagimu.",
    "Sagittarius": "Dunia memanggil. Rencanakan perjalanan atau pelajari filosofi baru.",
    "Capricorn": "Kerja kerasmu mulai terlihat. Tetap disiplin, puncak tujuan sudah dekat.",
    "Aquarius": "Ide-ide unikmu sangat berharga. Berbagilah dengan komunitasmu.",
    "Pisces": "Imajinasimu kuat. Salurkan lewat seni atau meditasi untuk ketenangan jiwa."
}

def main():
    print("\n=== PROGRAM CEK ZODIAK & RAMALAN ===")
    print("(Lokasi otomatis diatur oleh sistem)\n")
    nama_input = input("Masukkan Nama Lengkap : ")
    
    try:
        tgl_lahir = int(input("Tanggal Lahir (1-31)  : "))
        bln_lahir = int(input("Bulan Lahir (1-12)    : "))
        thn_lahir = int(input("Tahun Lahir (YYYY)    : "))
    except ValueError:
        print("\n[!] Error: Harap masukkan angka yang valid.")
        sys.exit()

    # 2. PROSES
    lat_fix = -6.2088
    lng_fix = 106.8456
    tz_fix = "Asia/Jakarta"

    try:
        subjek = AstrologicalSubject(
            nama_input, 
            thn_lahir, bln_lahir, tgl_lahir, 
            12, 00, 
            lat=lat_fix, lng=lng_fix, tz_str=tz_fix,
            city="Jakarta"
        )
        zodiak_raw = subjek.sun['sign']
        pesan_bulanan = "Maaf, ramalan belum tersedia."
        zodiak_display = zodiak_raw 
        for key in KATA_KATA:
            # Cek apakah Key Dict (Misal "Aries") DIAWALI oleh Output Library ("Ari")
            # "Aries".startswith("Ari") -> True
            if key.startswith(zodiak_raw): 
                pesan_bulanan = KATA_KATA[key]
                zodiak_display = key # Kita update jadi nama lengkap biar tampilan bagus
                break
        # -----------------------------------------------

        # 3. OUTPUT
        print("\n" + "="*40)
        print(f"Nama          : {subjek.name}")
        print(f"Tanggal Lahir : {tgl_lahir}-{bln_lahir}-{thn_lahir}")
        print("-" * 40)
        # Gunakan zodiak_display agar yang muncul "Aries" bukan "Ari"
        print(f"Zodiak Kamu   : {zodiak_display}") 
        print(f"Kata-kata     : \"{pesan_bulanan}\"")
        print("="*40 + "\n")

    except Exception as e:
        print(f"\n[!] Terjadi kesalahan sistem: {e}")

# if __name__ == "__main__":
    main()



# from pathlib import Path
# from kerykeion import AstrologicalSubjectFactory
# from kerykeion.chart_data_factory import ChartDataFactory
# from kerykeion.charts.chart_drawer import ChartDrawer

# # Create a subject from birth data (offline example with manual coordinates)
# subject = AstrologicalSubjectFactory.from_birth_data(
#     "Kanye", 1977, 6, 8, 8, 45,
#     lng=-84.38798,
#     lat=33.7490,
#     tz_str="America/New_York",
#     online=False,
# )

# # Pre-compute natal chart data (calculations only)
# chart_data = ChartDataFactory.create_natal_chart_data(subject)

# # Render and save the SVG
# drawer = ChartDrawer(chart_data=chart_data)
# out_dir = Path("charts_output")
# out_dir.mkdir(exist_ok=True)
# drawer.save_svg(output_path=out_dir, filename="kanye-natal")