#!/usr/bin/env python3
#------------------------------------------------------------------------------------------------------------------
# Program   : CrackStego
# Deskripsi : Program Python sederhana yang dirancang untuk meng-crack file stego dengan teknik Dictionary Attack.
# Pembuat   : fixploit03 
# Rilis     : 5-10-2024
# Github    : https://github.com/fixploit03/CrackStego/
#------------------------------------------------------------------------------------------------------------------
# MIT License
# 
# Copyright (c) 2024 fixploit03 
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#------------------------------------------------------------------------------------------------------------------

import os
import re
import subprocess           
import time
import platform
from datetime import datetime

## Variabel warna
m = "\033[31m" # Merah
h = "\033[32m" # Hijau 
k = "\033[33m" # Kuning 
b = "\033[34m" # Biru
c = "\033[36m" # Cyan
p = "\033[37m" # Putih 
r = "\033[0m"  # Reset 

# Cek sistem operasi 
sistem_operasi = platform.system()
# Android (Termux) & Linux
if sistem_operasi == "Linux":
    os.system("clear")
else:
    print(f"{p}[{m}-{p}] Sistem operasi Anda tidak mendukung untuk menjalankan program Steg2Crack.{r}")
    exit(1)
    
# Banner program 
print(f"""
{c}╔═╗╦═╗╔═╗╔═╗╦╔═  ╔═╗╔╦╗╔═╗╔═╗╔═╗{r}
{c}║  ╠╦╝╠═╣║  ╠╩╗  ╚═╗ ║ ║╣ ║ ╦║ ║{r}
{c}╚═╝╩╚═╩ ╩╚═╝╩ ╩  ╚═╝ ╩ ╚═╝╚═╝╚═╝{r}

{p}[{b}*{p}] Program   : {b}CrackStego{r}
{p}[{b}*{p}] Deskripsi : {b}Program Python untuk meng-crack file stego{r}
{p}[{b}*{p}] Pembuat   : {b}fixploit03{r}
{p}[{b}*{p}] Github    : {b}https://github.com/fixploit03/CrackStego/{r}
{p}[{b}*{p}] Team      : {b}ArSec (Arjuna Security){r}
""")

# Meminta nama file stego dari pengguna
while True:
    try:
        file_stego = input(f"{p}[{b}#{p}] Masukkan nama file stego : ")
        if not file_stego:
            print(f"{p}[{m}-{p}] File stego tidak boleh kosong.{r}")
            continue 
        if not os.path.isfile(file_stego):
            print(f"{p}[{m}-{p}] File stego '{file_stego}' tidak ditemukan.{r}")
            continue
        # Cek file stego
        if not file_stego.endswith((".jpg", ".jpeg", ".wav", ".au")):
            print(f"{p}[{m}-{p}] File '{file_stego}' bukan file stego.{r}")
            continue
        break
    except KeyboardInterrupt:
        print(f"\n{p}[{m}-{p}] Program dihentikan oleh pengguna.{r}")
        exit(1)
    except Exception as e:
        print(f"\n{p}[{m}-{p}] Terjadi kesalahan: {e}.{r}")
        exit(1)

# Meminta nama file wordlist dari pengguna
while True:
    try:
        file_wordlist = input(f"{p}[{b}#{p}] Masukkan nama file wordlist : ")
        if not file_wordlist:
            print(f"{p}[{m}-{p}] File wordlist tidak boleh kosong.{r}")
            continue 
        if not os.path.isfile(file_wordlist):
            print(f"{p}[{m}-{p}] File wordlist '{file_wordlist}' tidak ditemukan.{r}")
            continue
        # Cek file wordlist
        if not file_wordlist.endswith((".txt", ".lst")):
            print(f"{p}[{m}-{p}] File '{file_wordlist}' bukan file wordlist.{r}")
            continue
        break
    except KeyboardInterrupt:
        print(f"\n{p}[{m}-{p}] Program dihentikan oleh pengguna.{r}")
        exit(1)
    except Exception as e:
        print(f"\n{p}[{m}-{p}] Terjadi kesalahan: {e}.{r}")
        exit(1)

print("")

kata_sandi_ditemukan = False

# Proses cracking file stego
try:
    with open(file_wordlist, "r", encoding="latin-1", errors="ignore") as fw:
        daftar_kata_sandi = fw.read().splitlines()
        jumlah_kata_sandi = len(daftar_kata_sandi)
        waktu_mulai = datetime.now()
        print(f"{p}[{h}+{p}] Jumlah kata sandi yang terdapat dalam file wordlist : {h}{jumlah_kata_sandi}{r}")
        input(f"\n{p}Tekan [{h}Enter{p}] untuk memulai proses cracking...{r}")
        print(f"\n{p}[{b}*{p}] Dimulai pada : {b}{waktu_mulai.strftime('%d-%m-%Y %H:%M:%S')}{r}\n")
        time.sleep(3)
        for kata_sandi in daftar_kata_sandi:
            perintah_crack = f"steghide extract -sf {file_stego} -p {kata_sandi} -f"
            try:
                hasil_perintah_crack = subprocess.run(perintah_crack, shell=True, capture_output=True, text=True)
                if hasil_perintah_crack.returncode == 0:   
                    perintah_mencari_file_tersembunyi = f"steghide info {file_stego} -p {kata_sandi}"
                    hasil_perintah_mencari_file_tersembunyi = subprocess.run(perintah_mencari_file_tersembunyi, shell=True, capture_output=True, text=True)
                    if hasil_perintah_mencari_file_tersembunyi.returncode == 0:
                        pola = r'embedded file "(.*?)":'
                        cocok = re.search(pola, hasil_perintah_mencari_file_tersembunyi.stdout)
                        nama_file_tersembunyi = cocok.group(1).strip()
                    waktu_akhir = datetime.now()
                    print(f"{p}[{h}+{p}] Kata sandi ditemukan : {h}{kata_sandi}{r}") 
                    if os.path.isfile(nama_file_tersembunyi):
                        print(f"{p}[{h}+{p}] File yang disembunyikan : {h}{nama_file_tersembunyi}{r}") 
                    print(f"\n{p}[{b}*{p}] Berakhir pada : {b}{waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}{r}")
                    kata_sandi_ditemukan = True
                    break
                else:
                    print(f"{p}[{m}-{p}] Kata sandi salah : {m}{kata_sandi}{r}")
            except KeyboardInterrupt:
                print(f"\n{p}[{m}-{p}] Program dihentikan oleh pengguna.{r}")
                exit(1)
            except Exception as e:
                print(f"\n{p}[{m}-{p}] Terjadi kesalahan: {e}.{r}")
                exit(1)
        if not kata_sandi_ditemukan:
            waktu_akhir = datetime.now()
            print(f"{p}[{m}-{p}] Kata sandi tidak ditemukan, coba file Wordlist yang lain.{r}")
            print(f"\n{p}[{b}*{p}] Berakhir pada : {b}{waktu_akhir.strftime('%d-%m-%Y %H:%M:%S')}{r}")
except Exception as e:
    print(f"\n{p}[{m}-{p}] Terjadi kesalahan: {e}.{r}")
    exit(1)
