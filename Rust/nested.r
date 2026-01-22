input_nama <- function() {
  readline(prompt = "Masukkan nama anda: ")
}

input_nim <- function() {
  as.integer(readline(prompt = "Masukkan NIM anda: "))
}

input_kelas <- function() {
  # Menambahkan spasi setelah koma agar rapi
  daftar_kelas <- c("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
  cat("Kelas yang tersedia:", daftar_kelas, "\n")

  kelas_mahasiswa <- toupper(trimws(readline(prompt = "Masukkan kelas anda: ")))

  if (!(kelas_mahasiswa %in% daftar_kelas)) {
    cat("Kelas yang anda masukkan tidak ada dalam daftar\n")
    ulang <- tolower(trimws(readline(prompt = "Ulangi? (ya/tidak): ")))

    if (ulang == "ya") {
      # Memanggil fungsi diri sendiri (rekursif) tanpa kata kunci return
      input_kelas()
    } else {
      stop("Program dihentikan")
    }
  } else {
    # Mengembalikan nilai jika kondisi if di atas salah (else)
    kelas_mahasiswa
  }
}

hitung_grade <- function() {
  nilai_angka <- as.integer(readline(prompt = "Masukkan nilai angka (0-100): "))

  # Cek jika input bukan angka (NA)
  if (is.na(nilai_angka)) {
    stop("Input harus berupa angka!")
  }

  if (nilai_angka >= 80 && nilai_angka <= 100) {
    grade <- "A"
    keterangan <- "lulus"
  } else if (nilai_angka >= 68) {
    grade <- "B"
    keterangan <- "lulus"
  } else if (nilai_angka >= 56) {
    grade <- "C"
    keterangan <- "perbaikan"
  } else if (nilai_angka >= 46) {
    grade <- "D"
    keterangan <- "perbaikan"
  } else if (nilai_angka >= 0) {
    grade <- "E"
    keterangan <- "mengulang"
  } else {
    grade <- NA
    keterangan <- NA
  }

  # Membuat list sebagai output terakhir (implicit return)
  list(
    nilai_angka = nilai_angka,
    grade = grade,
    keterangan = keterangan
  )
}

# --- Eksekusi Utama ---
cat("--- Input Data Mahasiswa ---\n")
nama <- input_nama()
nim <- input_nim()
kelas <- input_kelas()
hasil <- hitung_grade()

cat("\n--- Hasil Akhir ---\n")
cat("Nama       :", nama, "\n")
cat("Kelas      :", paste0(kelas, "2025"), "\n")
cat("NIM        :", nim, "\n")
cat("Nilai      :", hasil$nilai_angka, "\n")
cat("Grade      :", hasil$grade, "\n")
cat("Keterangan :", hasil$keterangan, "\n")