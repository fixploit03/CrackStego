#!/usr/bin/env python3
#------------------------------------------------------------------------------------------------------------------
#  _____ _____  ______  _     ___ ___ _____ ___ _____  
# |  ___|_ _\ \/ /  _ \| |   / _ \_ _|_   _/ _ \___ /  
# | |_   | | \  /| |_) | |  | | | | |  | || | | ||_ \  
# |  _|  | | /  \|  __/| |__| |_| | |  | || |_| |__) | 
# |_|   |___/_/\_\_|   |_____\___/___| |_| \___/____/                                               
#------------------------------------------------------------------------------------------------------------------
# Program   : CrackStego
# Deskripsi : Program Python sederhana yang dirancang untuk meng-crack file stego dengan teknik Dictionary Attack.
# Pembuat   : fixploit03 
# Rilis     : 5-10-2024
# Github    : https://github.com/fixploit03/CrackStego/
#------------------------------------------------------------------------------------------------------------------
# Program ini dirancang hanya untuk tujuan pendidikan dan penelitian yang sah. Dilarang keras menggunakan program 
# ini untuk kegiatan ilegal, merusak, atau tanpa izin pemilik file. Pengguna bertanggung jawab penuh atas segala
# konsekuensi hukum yang mungkin timbul dari penggunaan program ini. Pastikan untuk selalu mematuhi peraturan dan 
# etika yang berlaku di wilayah Anda.
#------------------------------------------------------------------------------------------------------------------
# DILARANG KERAS UNTUK MENGUBAH DAN MEMUBLIKASIKAN DENGAN NAMA PRIBADI TANPA SEIZIN PEMBUAT. DIBUAT OPEN SOURCE
# AGAR DAPAT DISESUAIKAN DENGAN KEBUTUHAN MASING-MASING. SAYA TIDAK MELARANG UNTUK MENGEDIT KODE YANG ADA, AGAR
# KALIAN JUGA BISA BERKARYA.
#------------------------------------------------------------------------------------------------------------------
                              
# Import modul yang dibutuhkan 
import os
import re
import subprocess           
import time
import sys
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
    # File ID Linux
    file_id_linux = "/etc/os-release"
    perintah_mencari_id_linux = f"cat {file_id_linux}"
    try:
        mencari_id_linux = subprocess.run(perintah_mencari_id_linux, shell=True, capture_output=True, text=True)
        if mencari_id_linux.returncode == 0:
            hasil_mencari_id_linux = mencari_id_linux.stdout.strip()
            pola_file_id_linux = r'\bID=(\w+)'
            mencocokkan_pola_file_id_linux = re.search(pola_file_id_linux, mencari_id_linux.stdout)
            if mencocokkan_pola_file_id_linux:
                # ID Linux
                id_linux = mencocokkan_pola_file_id_linux.group(1).strip()
                if id_linux == "ubuntu" or id_linux == "debian":
                    print(f"[+] Sistem operasi : {sistem_operasi} ({id_linux})")
                else:
                      print("[-] Sistem operasi Anda tidak mendukung untuk menjalankan program CrackStego.")
                      sys.exit(1)
    except KeyboardInterrupt:
        print("\n[-] Program dihentikan oleh pengguna.")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Terjadi kesalahan : {e}.")
        sys.exit(1)
else:
    print("[-] Sistem operasi Anda tidak mendukung untuk menjalankan program CrackStego.")
    exit(1)
    
# Mengecek Steghide
print("[*] Mengecek Steghide...")
time.sleep(3)
perintah_cek_steghide = "steghide --version"
try:
    cek_steghide = subprocess.run(perintah_cek_steghide, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if cek_steghide.returncode == 0:
        print("[+] Steghide sudah terinstal.")
    else:
        print("[-] Steghide belum terinstal.")
        sistem_operasi = platform.system()
        if sistem_operasi == "Linux": 
            print("[-] Instal dengan mengetikkan perintah 'bash instal.sh'.")
            exit(1)
        else:
            print("[-] Sistem operasi Anda tidak mendukung untuk menjalankan program CrackStego.")
            exit(1)
except KeyboardInterrupt:
    print("\n[-] Program dihentikan oleh pengguna.")
    exit(1)
except Exception as e:
    print(f"[-] Terjadi kesalahan : {e}.")
    exit(1)

# Mengecek Stegseek
print("[*] Mengecek Stegseek...")
time.sleep(3)
perintah_cek_stegseek = "stegseek --version"
try:
    cek_stegseek = subprocess.run(perintah_cek_stegseek, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if cek_stegseek.returncode == 0:
        print("[+] Stegseek sudah terinstal.")
    else:
        print("[-] Stegseek belum terinstal.")
        sistem_operasi = platform.system()
        if sistem_operasi == "Linux": 
            print("[-] Instal dengan mengetikkan perintah 'bash instal.sh'.")
            exit(1)
        else:
            print("[-] Sistem operasi Anda tidak mendukung untuk menjalankan program CrackStego.")
            exit(1)
except KeyboardInterrupt:
    print("\n[-] Program dihentikan oleh pengguna.")
    exit(1)
except Exception as e:
    print(f"[-] Terjadi kesalahan : {e}.")
    exit(1)
  
# Mengecek Binutils
print("[*] Mengecek Binutils...")
time.sleep(3)
perintah_cek_binutils = "ld --version"
try:
    cek_binutils = subprocess.run(perintah_cek_binutils, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if cek_binutils.returncode == 0:
        print("[+] Binutils sudah terinstal.")
        input("\nTekan [Enter] untuk melanjutkan...")
        print("")
    else:
        print("[-] Binutils belum terinstal.")
        sistem_operasi = platform.system()
        if sistem_operasi == "Linux": 
            print("[-] Instal dengan mengetikkan perintah 'bash instal.sh'.")
            exit(1)
        else:
            print("[-] Sistem operasi Anda tidak mendukung untuk menjalankan program CrackStego.")
            exit(1)
except KeyboardInterrupt:
    print("\n[-] Program dihentikan oleh pengguna.")
    exit(1)
except Exception as e:
    print(f"[-] Terjadi kesalahan : {e}.")
    exit(1)
    
# Membersihkan layar terminal 
sistem_operasi = platform.system()
if sistem_operasi == "Linux":
    os.system("clear")
elif sistem_operasi == "Windows":
    os.system("cls")
else:
    print("[-] Sistem operasi Anda tidak mendukung untuk menjalankan program CrackStego.")
    exit(1)
    
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
        file_stego = input("[#] Masukkan nama file stego : ").strip().strip("'\"")
        print(f"[*] Mengecek file stego '{file_stego}'...")
        time.sleep(3)
        if not file_stego:
            print("[-] File stego tidak boleh kosong.")
            continue 
        if not os.path.isfile(file_stego):
            print(f"[-] File stego '{file_stego}' tidak ditemukan.")
            continue
        if not file_stego.lower().endswith((".jpg", ".jpeg", ".bmp", ".wav", ".au")):
            print(f"[-] File '{file_stego}' bukan file stego.")
            continue
        perintah_cek_file_stego = f"strings {file_stego}"
        try:
            cek_file_stego = subprocess.run(perintah_cek_file_stego, shell=True, capture_output=True, text=True)
            # Done
            if cek_file_stego.returncode == 0:
                hasil_cek_file_stego = cek_file_stego.stdout.strip()
                # pola_file_steghide = r"%&'\(\)\*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\n\s*#3R\n&'\(\)\*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz"
                if re.search(r"%&'\(\)\*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\n\s*#3R\n&'\(\)\*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz", hasil_cek_file_stego):
                    perintah_cek_enkripsi_file_stego = f"steghide extract -sf {file_stego} -p '' -f"
                    try:
                        cek_enkripsi_file_stego = subprocess.run(perintah_cek_enkripsi_file_stego, shell=True, capture_output=True, text=True)
                        # Done
                        if cek_enkripsi_file_stego.returncode ==0:
                            perintah_mencari_file_tersembunyi = f"steghide info {file_stego} -p ''"
                            try:
                                mencari_file_tersembunyi = subprocess.run(perintah_mencari_file_tersembunyi, shell=True, capture_output=True, text=True)
                                # Done 
                                if mencari_file_tersembunyi.returncode == 0:
                                    hasil_mencari_file_tersembunyi = mencari_file_tersembunyi.stdout.strip()
                                    # pola_file_tersembunyi = r'embedded file "(.*?)":'
                                    mencocokkan_pola_file_tersembunyi = re.search(r'embedded file "(.*?)":', hasil_mencari_file_tersembunyi)
                                    if mencocokkan_pola_file_tersembunyi:
                                        nama_file_tersembunyi = mencocokkan_pola_file_tersembunyi.group(1).strip()
                                        if os.path.isfile(nama_file_tersembunyi):
                                            try:
                                                os.remove(nama_file_tersembunyi)
                                                print(f"[-] File stego '{file_stego}' tidak dilindungi oleh kata sandi.")
                                                continue
                                            except KeyboardInterrupt:
                                                print("\n[-] Program dihentikan oleh pengguna.")
                                                exit(1)
                                            except Exception as e:
                                                print(f"[-] Terjadi kesalahan : {e}.")
                                            exit(1)
                            except KeyboardInterrupt:
                                print("\n[-] Program dihentikan oleh pengguna.")
                                exit(1)
                            except Exception as e:
                                print(f"[-] Terjadi kesalahan : {e}.")
                                exit(1)
                        else:
                            print(f"[+] File stego '{file_stego}' ditemukan.")
                            break
                    except KeyboardInterrupt:
                        print("\n[-] Program dihentikan oleh pengguna.")
                        exit(1)
                    except Exception as e:
                        print(f"[-] Terjadi kesalahan : {e}.")
                        exit(1)
                else:
                    print(f"[-] File '{file_stego}' bukan file stego.")
                    continue 
        except KeyboardInterrupt:
            print("\n[-] Program dihentikan oleh pengguna.")
            exit(1)
        except Exception as e:
            print(f"[-] Terjadi kesalahan : {e}.")
            exit(1)
    except KeyboardInterrupt:
        print("\n[-] Program dihentikan oleh pengguna.")
        exit(1)
    except Exception as e:
        print(f"\n[-] Terjadi kesalahan : {e}.")
        exit(1)

# Meminta nama file wordlist dari pengguna
while True:
    try:
        file_wordlist = input("[#] Masukkan nama file wordlist : ").strip().strip("'\"")
        print(f"[*] Mengecek file wordlist '{file_wordlist}'...")
        time.sleep(3)
        if not file_wordlist:
            print("[-] File wordlist tidak boleh kosong.")
            continue 
        if not os.path.isfile(file_wordlist):
            print(f"[-] File wordlist '{file_wordlist}' tidak ditemukan.")
            continue
        if not file_wordlist.lower().endswith((".txt", ".lst")):
            print(f"[-] File '{file_wordlist}' bukan file wordlist.")
            continue
        if os.stat(file_wordlist).st_size == 0:
            print(f"[-] File wordlist '{file_wordlist}' kosong.")
            continue 
        print(f"[+] File wordlist '{file_wordlist}' ditemukan.")
        break
    except KeyboardInterrupt:
        print("\n[-] Program dihentikan oleh pengguna.")
        exit(1)
    except Exception as e:
        print(f"\n[-] Terjadi kesalahan : {e}.")
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
            if kata_sandi == "":
                continue 
            perintah_crack_file_stego = f"steghide extract -sf {file_stego} -p {kata_sandi} -f"
            try:
                crack_file_stego = subprocess.run(perintah_crack_file_stego, shell=True, capture_output=True, text=True)
                # Done 
                if crack_file_stego.returncode == 0: 
                      perintah_mencari_file_tersembunyi = f"steghide info {file_stego} -p {kata_sandi}"
                      mencari_file_tersembunyi = subprocess.run(perintah_mencari_file_tersembunyi, shell=True, capture_output=True, text=True)
                      # Done 
                      if mencari_file_tersembunyi.returncode == 0:
                          pola_file_tersembunyi = r'embedded file "(.*?)":'
                          mencocokkan_pola_file_tersembunyi = re.search(pola_file_tersembunyi, mencari_file_tersembunyi.stdout)
                          if mencocokkan_pola_file_tersembunyi:
                              nama_file_tersembunyi = mencocokkan_pola_file_tersembunyi.group(1).strip()
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
                print(f"\n[-] Terjadi kesalahan : {e}.")
                exit(1)
        if not kata_sandi_ditemukan:
            waktu_akhir = datetime.now()
            print(f"[-] Kata sandi tidak ditemukan. Silakan coba file wordlist yang lain.")
            print(f"\n[*] Berakhir pada : {waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}")
except Exception as e:
    print(f"\n[-] Terjadi kesalahan : {e}.")
    exit(1)
