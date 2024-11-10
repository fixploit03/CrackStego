file_path = input("Masukkan path file stego: ")

# Menghapus tanda petik tunggal di awal dan akhir jika ada
if file_path.startswith("'") and file_path.endswith("'"):
    file_path = file_path[1:-1]

print(f"Path yang digunakan: {file_path}")

# Lanjutkan proses hanya jika file ada
import os
if os.path.isfile(file_path):
    print("File ditemukan. Melanjutkan proses...")
else:
    print("Error: File tidak ditemukan.")
  
