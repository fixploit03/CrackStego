#!/usr/bin/env python3
#------------------------------------------------------------------------------------------------------------------
# Program   : CrackStego
# Deskripsi : Program Python sederhana yang dirancang untuk meng-crack file stego dengan teknik Dictionary Attack.
# Pembuat   : fixploit03 
# Rilis     : 5-10-2024
# Github    : https://github.com/fixploit03/CrackStego/
#------------------------------------------------------------------------------------------------------------------

import os
import re
import subprocess           
import time
import platform
from datetime import datetime

## Variabel warna
k = "\033[33m" # Kuning 
p = "\033[37m" # Putih 
r = "\033[0m"  # Reset 

# Banner selamat datang
print(f"""
{k}Selamat datang di CrackStego{r}

{k}Peringatan{r}
{p}----------{r}
{p}Program ini dirancang hanya untuk tujuan pendidikan dan penelitian yang sah.{r}
{p}Dilarang keras menggunakan program ini untuk kegiatan ilegal, merusak,{r}
{p}atau tanpa izin pemilik file. Pengguna bertanggung jawab penuh atas segala{r}
{p}konsekuensi hukum yang mungkin timbul dari penggunaan program ini. Pastikan{r}
{p}untuk selalu mematuhi peraturan dan etika yang berlaku di wilayah Anda.{r}
""")
time.sleep(3)

# Mengecek sistem operasi
print(f"{p}[{k}*{p}] {p}Mengecek sistem operasi...{r}")
time.sleep(3)
sistem_operasi = platform.system()
if sistem_operasi == "Linux":
    print(f"{p}[{k}+{p}] Sistem operasi : {k}{sistem_operasi}{r}")
else:
    print(f"{p}[{k}-{p}] Sistem operasi Anda tidak mendukung untuk menjalankan program CrackStego.{r}")
    exit(1)

# Mengecek Steghide
print(f"{p}[{k}*{p}] Mengecek Steghide...{r}")
time.sleep(3)
perintah_cek_steghide = f"steghide --version"
try:
    cek_file_steghide = subprocess.run(perintah_cek_steghide, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if cek_file_steghide.returncode == 0:
        print(f"{p}[{k}+{p}] Steghide sudah terinstal.{r}")
    else:
        print(f"{p}[{k}-{p}] Steghide belum terinstal.{r}")
        print(f"{p}[{k}-{p}] Instal dengan mengetikkan perintah 'sudo apt-get install steghide'.{r}")
        exit(1)
except KeyboardInterrupt:
    print(f"\n{p}[{k}-{p}] Program dihentikan oleh pengguna.{r}")
    exit(1)
except Exception as e:
    print(f"{p}[{k}-{p}] Terjadi kesalahan: {e}{r}")
    exit(1)

# Mengecek Binutils
print(f"{p}[{k}*{p}] Mengecek Binutils...{r}")
time.sleep(3)
perintah_cek_binutils = f"ld --version"
try:
    cek_file_binutils = subprocess.run(perintah_cek_binutils, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if cek_file_binutils.returncode == 0:
        print(f"{p}[{k}+{p}] Binutils sudah terinstal.{r}")
        input(f"\n{p}Tekan [{k}Enter{p}] untuk melanjutkan...{r}")
    else:
        print(f"{p}[{k}-{p}] Binutils belum terinstal.{r}")
        print(f"{p}[{k}-{p}] Instal dengan mengetikkan perintah 'sudo apt-get install binutils'.{r}")
        exit(1)
except KeyboardInterrupt:
    print(f"\n{p}[{k}-{p}] Program dihentikan oleh pengguna.{r}")
    exit(1)
except Exception as e:
    print(f"{p}[{k}-{p}] Terjadi kesalahan: {e}{r}")
    exit(1)

# Membersihkan layar terminal
os.system("clear")

# Banner program 
print(f"""
             {k}╔═╗╦═╗╔═╗╔═╗╦╔═  ╔═╗╔╦╗╔═╗╔═╗╔═╗{r}
             {k}║  ╠╦╝╠═╣║  ╠╩╗  ╚═╗ ║ ║╣ ║ ╦║ ║{r}
             {k}╚═╝╩╚═╩ ╩╚═╝╩ ╩  ╚═╝ ╩ ╚═╝╚═╝╚═╝{r}

{p}[{k}*{p}] Program   : {k}CrackStego{r}
{p}[{k}*{p}] Deskripsi : {k}Program Python untuk meng-crack file stego{r}
{p}[{k}*{p}] Pembuat   : {k}fixploit03{r}
{p}[{k}*{p}] Github    : {k}https://github.com/fixploit03/CrackStego/{r}
{p}[{k}*{p}] Team      : {k}ArSec (Arjuna Security){r}
""")

# Meminta nama file stego dari pengguna
while True:
    try:
        file_stego = input(f"{p}[{k}#{p}] Masukkan nama file stego : {k}")
        print(f"{p}[{k}*{p}] Mengecek file stego '{file_stego}'...{r}")
        time.sleep(3)
        if not file_stego:
            print(f"{p}[{k}-{p}] File stego tidak boleh kosong.{r}")
            continue 
        if not os.path.isfile(file_stego):
            print(f"{p}[{k}-{p}] File stego '{file_stego}' tidak ditemukan.{r}")
            continue
        if not file_stego.endswith((".jpg", ".jpeg", ".wav", ".au")):
            print(f"{p}[{k}-{p}] File '{file_stego}' bukan file stego.{r}")
            continue
        perintah_cek_file_stego = f"strings {file_stego}"
        try:
            cek_file_stego = subprocess.run(perintah_cek_file_stego, shell=True, capture_output=True, text=True)
            if cek_file_stego.returncode == 0:
                pola_file_steghide = r"%&'\(\)\*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\n\s*#3R\n&'\(\)\*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz"
                if re.search(pola_file_steghide, cek_file_stego.stdout):
                    print(f"{p}[{k}+{p}] File stego '{file_stego}' ditemukan.{r}")
                    break
                else:
                    print(f"{p}[{k}-{p}] File '{file_stego}' bukan file stego.{r}")
                    continue 
        except KeyboardInterrupt:
            print(f"\n{p}[{k}-{p}] Program dihentikan oleh pengguna.{r}")
            exit(1)
        except Exception as e:
            print(f"{p}[{k}-{p}] Terjadi kesalahan: {e}{r}")
            exit(1)
    except KeyboardInterrupt:
        print(f"\n{p}[{k}-{p}] Program dihentikan oleh pengguna.{r}")
        exit(1)
    except Exception as e:
        print(f"\n{p}[{m}-{p}] Terjadi kesalahan: {e}.{r}")
        exit(1)

# Meminta nama file wordlist dari pengguna
while True:
    try:
        file_wordlist = input(f"{p}[{k}#{p}] Masukkan nama file wordlist : {k}")
        print(f"{p}[{k}*{p}] Mengecek file wordlist '{file_wordlist}'...{r}")
        time.sleep(3)
        if not file_wordlist:
            print(f"{p}[{k}-{p}] File wordlist tidak boleh kosong.{r}")
            continue 
        if not os.path.isfile(file_wordlist):
            print(f"{p}[{k}-{p}] File wordlist '{file_wordlist}' tidak ditemukan.{r}")
            continue
        if not file_wordlist.endswith((".txt", ".lst")):
            print(f"{p}[{k}-{p}] File '{file_wordlist}' bukan file wordlist.{r}")
            continue
        print(f"{p}[{k}+{p}] File wordlist '{file_wordlist}' ditemukan.{r}")
        break
    except KeyboardInterrupt:
        print(f"\n{p}[{k}-{p}] Program dihentikan oleh pengguna.{r}")
        exit(1)
    except Exception as e:
        print(f"\n{p}[{k}-{p}] Terjadi kesalahan: {e}.{r}")
        exit(1)

print("")

kata_sandi_ditemukan = False

# Proses cracking file stego
try:
    with open(file_wordlist, "r", encoding="latin-1", errors="ignore") as fw:
        daftar_kata_sandi = fw.read().splitlines()
        jumlah_kata_sandi = len(daftar_kata_sandi)
        waktu_mulai = datetime.now()
        print(f"{p}[{k}+{p}] Jumlah kata sandi yang terdapat dalam file wordlist : {k}{jumlah_kata_sandi}{r}")
        input(f"\n{p}Tekan [{k}Enter{p}] untuk memulai proses cracking...{r}")
        print(f"\n{p}[{k}*{p}] Dimulai pada : {k}{waktu_mulai.strftime('%d-%m-%Y %H:%M:%S')}{r}\n")
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
                    print(f"{p}[{k}+{p}] Kata sandi ditemukan : {k}{kata_sandi}{r}") 
                    if os.path.isfile(nama_file_tersembunyi):
                        print(f"{p}[{k}+{p}] File yang disembunyikan : {k}{nama_file_tersembunyi}{r}") 
                    print(f"\n{p}[{k}*{p}] Berakhir pada : {k}{waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}{r}")
                    kata_sandi_ditemukan = True
                    break
                else:
                    print(f"{p}[{k}-{p}] Kata sandi salah : {k}{kata_sandi}{r}")
            except KeyboardInterrupt:
                print(f"\n{p}[{k}-{p}] Program dihentikan oleh pengguna.{r}")
                exit(1)
            except Exception as e:
                print(f"\n{p}[{k}-{p}] Terjadi kesalahan: {e}.{r}")
                exit(1)
        if not kata_sandi_ditemukan:
            waktu_akhir = datetime.now()
            print(f"{p}[{k}-{p}] Kata sandi tidak ditemukan, coba file Wordlist yang lain.{r}")
            print(f"\n{p}[{k}*{p}] Berakhir pada : {k}{waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}{r}")
except Exception as e:
    print(f"\n{p}[{k}-{p}] Terjadi kesalahan: {e}.{r}")
    exit(1)
