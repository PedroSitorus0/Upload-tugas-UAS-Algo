def input_nama():
    nama_mahasiswa = input("Masukkan nama anda: ").strip()
    
    # 1. Cek kosong
    if nama_mahasiswa == "":
        print("Nama tidak boleh kosong")
        if input("Apakah anda ingin mengulanginya? (ya/tidak): ").strip().lower() == "ya":
            return input_nama()  # Rekursi
        else:
            exit()
    
    temp_nama = nama_mahasiswa.replace(" ", "").replace("-", "").replace("'", "")
    if not temp_nama.isalpha():
        print("Nama tidak boleh mengandung simbol atau angka")
        if input("Apakah anda ingin mengulanginya? (ya/tidak): ").strip().lower() == "ya":
            return input_nama() 
        else:
            exit()
    
    # 3. Cek panjang minimal
    if len(nama_mahasiswa) < 3:
        print("Nama tidak boleh kurang dari 3 karakter")
        if input("Apakah anda ingin mengulanginya? (ya/tidak): ").strip().lower() == "ya":
            return input_nama() 
        else:
            exit()
    
    return nama_mahasiswa

def input_nim():
    nim_mahasiswa = int(input("Masukkan NIM anda: "))
    if len(str(nim_mahasiswa)) != 9:
        print("NIM harus terdiri dari 10 digit angka.")
        if input("apakah anda ingin mengulanginya? (ya/tidak):").strip().lower() == "ya":
            return input_nim()
        else:
            exit()
    return nim_mahasiswa

def input_kelas():
    daftar_kelas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print("Kelas yang tersedia:", daftar_kelas)
    kelas_mahasiswa = input("Masukkan kelas anda: ").strip().upper()
    if kelas_mahasiswa not in daftar_kelas:
        print("kelas yang anda masukan tidak ada dalam daftar")
        if input("apakah anda ingin mengulanginya? (ya/tidak):").strip().lower() == "ya":
            return input_kelas()
        else:
            exit()
    return kelas_mahasiswa

def hitung_grade():
    nilai_angka = int(input("Masukkan nilai angka (0-100): "))
    grade = "" 
    
    if 80 <= nilai_angka <= 100:
        grade = "A"
        keterangan = "lulus"
    elif 68 <= nilai_angka < 80: 
        grade = "B"
        keterangan = "lulus"
    elif 56 <= nilai_angka < 68:
        grade = "C"
        keterangan = "perbaikan"
    elif 46 <= nilai_angka < 56:
        grade = "D"
        keterangan ="perbaikan"
    elif 0 <= nilai_angka < 46: 
        grade = "E"
        keterangan = "mengulang"
    else:
        grade = nilai_angka 

    return nilai_angka, grade, keterangan 

print("--- Input Data Mahasiswa ---")
nama = input_nama()
nim = input_nim()
kelas = input_kelas()
nilai_akhir, grade_huruf, keterangan = hitung_grade()

# print("\n--- Hasil Akhir ---")
# print(f"Nama  : {nama}")
# print(f"Kelas : {kelas}2025")
# print(f"NIM   : {nim}")
# print(f"Nilai : {nilai_akhir}")
# print(f"Grade: {grade_huruf}")
# print(f"Keterangan: {keterangan}")


def nilai_mahasiswa(nama, nim, kelas, nilai_akhir, grade_huruf, keterangan):
    print("\n--- Hasil Akhir ---")
    print(f"Nama  : {nama}")
    print(f"Kelas : {kelas}2025")
    print(f"NIM   : {nim}")
    print(f"Nilai : {nilai_akhir}")
    print(f"Grade: {grade_huruf}")
    print(f"Keterangan: {keterangan}")

nilai_mahasiswa(nama, nim, kelas, nilai_akhir, grade_huruf, keterangan)

# def log( user, password, akses):
#     print(user, passwo, akses)

# ussemane = "admin"
# password = "admin123"
# akses = "superuser"
# log(ussemane, password, akses)