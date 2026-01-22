# print("--- Toko Sembako Pak Abdulah ---")

# email = input("Masukkan email: ")
# sandi = input("Masukkan sandi: ")

# if email == "tes@gmail.com":
#     try:
#         sandi = int(sandi)
#         if sandi == 1234:
#             print("Anda berhasil login")
#         else:
#             print("Sandi salah")
#     except ValueError:
#         print("sandi anda salah")
# else:
#     print("Anda belum terdaftar, ingin registrasi?")

print("--- Website    ---")

email = input("Masukkan email: ")
sandi = input("Masukkan sandi: ")

if email == "tes@gmail.com":
    if sandi == "1234":
        print("Anda berhasil login")
    else:
        print("Sandi salah")
else:
    print("Anda belum terdaftar, ingin registrasi?")
    if input("Ingin registrasi? (ya/tidak): ").strip().lower() == "ya":
        new_email = input("Masukkan email baru: ")
        new_sandi = input("Masukkan sandi baru: ")
        print("Registrasi berhasil! Silakan login dengan email dan sandi baru Anda.")
