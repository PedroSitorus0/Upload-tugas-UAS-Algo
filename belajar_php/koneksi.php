<?php
$hostname = "localhost";
$user_db  = "root";
$pass_db  = "PASSWORD_MARIADB_ANDA"; // <--- GANTI INI dengan password yang Anda buat tadi
$nama_db  = "belajar_php";

// Mencoba menghubungkan (seperti handshake)
$conn = mysqli_connect($hostname, $user_db, $pass_db, $nama_db);

// Cek apakah koneksi gagal?
if (!$conn) {
    die("Koneksi ke Database Gagal: " . mysqli_connect_error());
}
?>