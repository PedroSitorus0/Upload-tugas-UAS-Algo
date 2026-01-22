def hitung_grade_dan_keterangan(nilai):
    """Fungsi untuk menentukan grade dan keterangan berdasarkan nilai"""
    if nilai >= 80:
        grade = "A"
        keterangan = "Lulus"
    elif nilai >= 68 and nilai <80:
        grade = "B"
        keterangan = "Lulus"
    elif nilai >= 56 and nilai <68:
        grade = "C"
        keterangan = "Perbaikan"
    elif nilai >= 46 and nilai <56:
        grade = "D"
        keterangan = "Perbaikan"
    elif nilai <46:
        grade = "E"
        keterangan = "Tidak lulus"
    
    return grade, keterangan

def tampilkan_data_mahasiswa(nama, kelas, nim, nilai):
    """Fungsi untuk menampilkan data mahasiswa"""
    grade, keterangan = hitung_grade_dan_keterangan(nilai)
    
    print("\n--- Output ---")
    print(f"Nama Siswa : {nama}")
    print(f"Kelas Siswa : {kelas}")
    print(f"Nim Siswa : {nim}")
    print(f"Nilai Siswa : {nilai}")
    print(f"Grade : {grade}")
    print(f"Keterangan : {keterangan}")


nama = input("Masukan Nama Anda: ")
kelas = input("Masukan kelas anda: ")
nim = int(input("masukan NIM anda: "))
nilai = int(input("masukan nilai anda: "))

tampilkan_data_mahasiswa(nama, kelas, nim, nilai)