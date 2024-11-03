#!/usr/bin/env python3
#------------------------------------------------------------------------------------------------------------------
# Program   : CrackStego
# Deskripsi : Program Python sederhana yang dirancang untuk meng-crack file stego dengan teknik Dictionary Attack.
# Pembuat   : fixploit03 
# Rilis     : 5-10-2024
# Github    : https://github.com/fixploit03/CrackStego/
#------------------------------------------------------------------------------------------------------------------

# Import modul yang dibutuhkan 
import os
import re
import subprocess           
import time
import platform
from datetime import datetime

# Banner selamat datang
print(f"""
Selamat datang di CrackStego

Peringatan
----------
Program ini dirancang hanya untuk tujuan pendidikan dan penelitian yang sah.
Dilarang keras menggunakan program ini untuk kegiatan ilegal, merusak,
atau tanpa izin pemilik file. Pengguna bertanggung jawab penuh atas segala
konsekuensi hukum yang mungkin timbul dari penggunaan program ini. Pastikan
untuk selalu mematuhi peraturan dan etika yang berlaku di wilayah Anda.
""")
time.sleep(3)

# Mengecek sistem operasi
print("[*] Mengecek sistem operasi...")
time.sleep(3)
sistem_operasi = platform.system()
if sistem_operasi == "Linux":
    print(f"[+] Sistem operasi : {sistem_operasi}")
elif sistem_operasi == "Windows":
    print(f"[+] Sistem operasi : {sistem_operasi}")
else:
    print("[-] Sistem operasi Anda tidak mendukung untuk menjalankan program CrackStego.")
    exit(1)

# Mengecek Steghide
print("[*] Mengecek Steghide...")
time.sleep(3)
perintah_cek_steghide = "steghide --version"
try:
    cek_file_steghide = subprocess.run(perintah_cek_steghide, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if cek_file_steghide.returncode == 0:
        print("[+] Steghide sudah terinstal.")
    else:
        print("[-] Steghide belum terinstal.")
        if sistem_operasi == "Linux":
            print("[-] Instal dengan mengetikkan perintah 'sudo apt-get install steghide'.")
        elif sistem_operasi == "Windows":
            print("[-] Instal dari 'https://steghide.sourceforge.net/download.php'.")
        exit(1)
except KeyboardInterrupt:
    print("\n[-] Program dihentikan oleh pengguna.")
    exit(1)
except Exception as e:
    print(f"[-] Terjadi kesalahan: {e}.")
    exit(1)

# Mengecek Binutils
print("[*] Mengecek Binutils...")
time.sleep(3)
perintah_cek_binutils = "ld --version"
try:
    cek_file_binutils = subprocess.run(perintah_cek_binutils, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if cek_file_binutils.returncode == 0:
        print("[+] Binutils sudah terinstal.")
        input("\nTekan [Enter] untuk melanjutkan...")
        print("")
    else:
        print("[-] Binutils belum terinstal.")
        if sistem_operasi == "Linux":
            print("[-] Instal dengan mengetikkan perintah 'sudo apt-get install binutils'.")
        elif sistem_operasi == "Windows":
            print("[-] Instal dari 'https://www.msys2.org/'.")
        exit(1)
except KeyboardInterrupt:
    print("\n[-] Program dihentikan oleh pengguna.")
    exit(1)
except Exception as e:
    print(f"[-] Terjadi kesalahan: {e}.")
    exit(1)

# Membersihkan layar terminal 
if sistem_operasi == "Linux":
    os.system("clear")
elif sistem_operasi == "Windows":
    os.system("cls")

# Banner program 
print("""
              ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╔╦╗╔═╗╔═╗╔═╗
              ║  ╠╦╝╠═╣║  ╠╩╗╚═╗ ║ ║╣ ║ ╦║ ║
              ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝ ╩ ╚═╝╚═╝╚═╝

[*] Program   : CrackStego
[*] Deskripsi : Program Python untuk meng-crack file stego
[*] Pembuat   : fixploit03
[*] Github    : https://github.com/fixploit03/CrackStego/
[*] Team      : ArSec (Arjuna Security)
""")

# Meminta nama file stego dari pengguna
while True:
    try:
        file_stego = input("[#] Masukkan nama file stego : ")
        print(f"[*] Mengecek file stego '{file_stego}'...")
        time.sleep(3)
        if not file_stego:
            print("[-] File stego tidak boleh kosong.")
            continue 
        if not os.path.isfile(file_stego):
            print(f"[-] File stego '{file_stego}' tidak ditemukan.")
            continue
        if not file_stego.endswith((".jpg", ".jpeg", ".wav", ".au")):
            print(f"[-] File '{file_stego}' bukan file stego.")
            continue
        perintah_cek_file_stego = f"strings {file_stego}"
        try:
            cek_file_stego = subprocess.run(perintah_cek_file_stego, shell=True, capture_output=True, text=True)
            if cek_file_stego.returncode == 0:
                pola_file_steghide = r"%&'\(\)\*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\n\s*#3R\n&'\(\)\*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz"
                if re.search(pola_file_steghide, cek_file_stego.stdout):
                    print(f"[+] File stego '{file_stego}' ditemukan.")
                    break
                else:
                    print(f"[-] File '{file_stego}' bukan file stego.")
                    continue 
        except KeyboardInterrupt:
            print("\n[-] Program dihentikan oleh pengguna.")
            exit(1)
        except Exception as e:
            print(f"[-] Terjadi kesalahan: {e}.")
            exit(1)
    except KeyboardInterrupt:
        print("\n[-] Program dihentikan oleh pengguna.")
        exit(1)
    except Exception as e:
        print(f"\n[-] Terjadi kesalahan: {e}.")
        exit(1)

# Meminta nama file wordlist dari pengguna
while True:
    try:
        file_wordlist = input("[#] Masukkan nama file wordlist : ")
        print(f"[*] Mengecek file wordlist '{file_wordlist}'...")
        time.sleep(3)
        if not file_wordlist:
            print("[-] File wordlist tidak boleh kosong.")
            continue 
        if not os.path.isfile(file_wordlist):
            print(f"[-] File wordlist '{file_wordlist}' tidak ditemukan.")
            continue
        if not file_wordlist.endswith((".txt", ".lst")):
            print(f"[-] File '{file_wordlist}' bukan file wordlist.")
            continue
        print(f"[+] File wordlist '{file_wordlist}' ditemukan.")
        break
    except KeyboardInterrupt:
        print("\n[-] Program dihentikan oleh pengguna.")
        exit(1)
    except Exception as e:
        print(f"\n[-] Terjadi kesalahan: {e}.")
        exit(1)

print("")

kata_sandi_ditemukan = False

# Proses cracking file stego
try:
    with open(file_wordlist, "r", encoding="latin-1", errors="ignore") as fw:
        daftar_kata_sandi = fw.read().splitlines()
        jumlah_kata_sandi = len(daftar_kata_sandi)
        waktu_mulai = datetime.now()
        print(f"[+] Jumlah kata sandi yang terdapat dalam file wordlist : {jumlah_kata_sandi}")
        input("\nTekan [Enter] untuk memulai proses cracking...")
        print(f"\n[*] Dimulai pada : {waktu_mulai.strftime('%d-%m-%Y %H:%M:%S')}\n")
        time.sleep(3)
        for kata_sandi in daftar_kata_sandi:
            perintah_crack_file_stego = f"steghide extract -sf {file_stego} -p {kata_sandi} -f"
            try:
                crack_file_stego = subprocess.run(perintah_crack_file_stego, shell=True, capture_output=True, text=True)
                if crack_file_stego.returncode == 0:   
                    perintah_mencari_file_tersembunyi = f"steghide info {file_stego} -p {kata_sandi}"
                    mencari_file_tersembunyi = subprocess.run(perintah_mencari_file_tersembunyi, shell=True, capture_output=True, text=True)
                    if mencari_file_tersembunyi.returncode == 0:
                        pola = r'embedded file "(.*?)":'
                        cocok = re.search(pola, mencari_file_tersembunyi.stdout)
                        if cocok:
                            nama_file_tersembunyi = cocok.group(1).strip()
                    waktu_akhir = datetime.now()
                    print(f"[+] Kata sandi ditemukan : {kata_sandi}") 
                    if os.path.isfile(nama_file_tersembunyi):
                        print(f"[+] File yang disembunyikan : {nama_file_tersembunyi}") 
                    print(f"\n[*] Berakhir pada : {waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}")
                    kata_sandi_ditemukan = True
                    break
                else:
                    print(f"[-] Kata sandi salah : {kata_sandi}")
            except KeyboardInterrupt:
                print("\n[-] Program dihentikan oleh pengguna.")
                exit(1)
            except Exception as e:
                print(f"\n[-] Terjadi kesalahan: {e}.")
                exit(1)
        if not kata_sandi_ditemukan:
            waktu_akhir = datetime.now()
            print("[-] Kata sandi tidak ditemukan, coba file Wordlist yang lain.")
            print(f"\n[*] Berakhir pada : {waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}")
except Exception as e:
    print(f"\n[-] Terjadi kesalahan: {e}.")
    exit(1)
