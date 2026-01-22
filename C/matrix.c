#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // Library untuk fungsi usleep (delay)

int main() {
    int i, r, len;
    
    // Mengubah warna teks terminal menjadi Hijau Terang (\033[1;32m)
    printf("\033[1;32m");

    while (1) { // Loop selamanya (Infinite Loop)
        
        // Membuat panjang baris acak
        len = rand() % 50 + 1; 

        for (i = 0; i < len; i++) {
            // Membuat karakter acak (angka atau huruf)
            // Kita pakai teknik sederhana: cetak karakter ASCII
            r = rand() % 2; // Hanya angka 0 atau 1 agar mirip biner
            
            if (r == 0) {
                printf("0 ");
            } else {
                printf("1 ");
            }
        }

        // Pindah baris
        printf("\n");

        // Delay sebentar agar mata bisa mengikuti (50000 mikrosedetik = 0.05 detik)
        usleep(50000); 
    }

    // Mengembalikan warna terminal ke normal (putih/default)
    printf("\033[0m");
    
    return 0;
}