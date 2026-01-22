import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Pilih pivot dari tengah
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def main():
    """Fungsi utama program."""
    print("=" * 50)
    print("PROGRAM QUICK SORT")
    print("=" * 50)
    
    # Opsi input
    print("Pilih sumber data:")
    print("1. Input manual")
    print("2. Gunakan contoh data")
    
    pilihan = input("\nMasukkan pilihan (1/2): ")
    
    if pilihan == "1":
        # Input manual dari pengguna
        while True:
            try:
                input_str = input("\nMasukkan angka-angka (pisahkan dengan spasi): ")
                if not input_str.strip():
                    print("Input tidak boleh kosong!")
                    continue
                    
                data = [float(x) if '.' in x else int(x) for x in input_str.split()]
                break
            except ValueError:
                print("Error: Harap masukkan angka yang valid!")
    
    else:
        # Menggunakan contoh data
        data = [64, 34, 25, 12, 22, 11, 90, 77, 45, 33, 88, 51]
        print(f"\nMenggunakan contoh data: {data}")
    
    # Tampilkan data asli
    print(f"\n{'='*50}")
    print(f"Data sebelum diurutkan: {data}")
    
    # Proses sorting
    try:
        sorted_data = quick_sort(data)
        
        # Tampilkan hasil
        print(f"Data setelah diurutkan: {sorted_data}")
        
        # Informasi tambahan
        print(f"\nInformasi:")
        print(f"- Jumlah elemen: {len(sorted_data)}")
        print(f"- Nilai minimum: {sorted_data[0]}")
        print(f"- Nilai maksimum: {sorted_data[-1]}")
        
        # Tampilkan perbedaan
        if pilihan != "1":  # Jika menggunakan contoh data
            print(f"\nContoh penggunaan:")
            test_data = [3, 6, 8, 10, 1, 2, 1]
            print(f"  quick_sort({test_data})")
            print(f"  Hasil: {quick_sort(test_data)}")
    
    except Exception as e:
        print(f"Terjadi error saat sorting: {e}")
    
    print(f"\n{'='*50}")
    print("Program selesai. Terima kasih!")


if __name__ == "__main__":
    main()