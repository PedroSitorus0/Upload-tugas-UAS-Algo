#include <stdio.h>
#include <string.h> 

int main() {
    int i;
    int jumlah_siswa;
    int nilai;
    char grade;          
    char keterangan[50]; 

    // Tambahkan \n agar teks tidak menumpuk ke samping
    printf("--- Selamat datang pada database nilai siswa ---\n");
    printf("Silahkan masukan jumlah siswa yang ingin anda masukan: ");
    
    // PERBAIKAN 1: Gunakan %d, bukan &
    scanf("%d", &jumlah_siswa);

    for (i = 1; i <= jumlah_siswa; i++) {
        printf("\nMasukkan nilai angka siswa ke-%d: ", i);
        scanf("%d", &nilai);

        // Logika Penilaian
        if (nilai >= 69 && nilai <= 75) {
            grade = 'A'; 
            strcpy(keterangan, "Sangat Memuaskan"); 
        } 
        else if (nilai < 69) {
            grade = 'B';
            strcpy(keterangan, "Cukup, perlu belajar lagi");
        }
        else {
            grade = 'S'; 
            strcpy(keterangan, "Luar Biasa!");
        }

        // Output
        printf("=== Hasil ===\n");
        printf("Siswa ke    : %d\n", i); // Typo 'Siwa' diperbaiki jadi 'Siswa'
        printf("Nilai Angka : %d\n", nilai);
        printf("Grade       : %c\n", grade);       
        printf("Keterangan  : %s\n", keterangan);  
        
        // PERBAIKAN 2: return 0 JANGAN ditaruh di sini
    } // Akhir dari Loop For

    return 0; // Taruh di sini (artinya program selesai setelah SEMUA loop beres)
}

