# CrackStego

[![versi](https://img.shields.io/badge/versi-1.0.0-blue)](https://github.com/fixploit03/CrackStego/releases)
[![lisensi](https://img.shields.io/badge/lisensi-MIT-green)](https://github.com/fixploit03/CrackStego/blob/main/LICENSE)
[![versi python](https://img.shields.io/badge/python-%E2%89%A5%203.6-blue.svg)](https://www.python.org/)
[![dipelihara](https://img.shields.io/badge/Dipelihara-Ya-96c40f)](https://img.shields.io/badge/Dipelihara-Ya-96c40f)
[![dikembangan di kali linux](https://img.shields.io/badge/Dikembangkan%20di-Kali%20Linux-blueviolet)](https://www.kali.org/)

`CrackStego` adalah program Python yang dirancang untuk meng-crack file stego yang dihasilkan oleh [Steghide](https://steghide.sourceforge.net/) dengan menggunakan teknik serangan [Dictionary Attack](https://www.asdf.id/definisi-dictionary-attack-adalah/).

> **Disclaimer**: Program ini dirancang hanya untuk tujuan pendidikan dan penelitian yang sah. Dilarang keras menggunakan program ini untuk kegiatan ilegal, merusak, atau tanpa izin pemilik file. Pengguna bertanggung jawab penuh atas segala konsekuensi hukum yang mungkin timbul dari penggunaan program ini. Pastikan untuk selalu mematuhi peraturan dan etika yang berlaku di wilayah Anda.

## Apa Itu File Stego?

File stego adalah file yang telah disisipkan informasi tersembunyi menggunakan teknik steganografi. Steganografi adalah metode untuk menyembunyikan data di dalam file lain, seperti gambar atau audio, sehingga keberadaan data tersebut tidak mudah terdeteksi.

Untuk penjelasan yang lebih lengkap, silakan tonton video ini:

> - [INI RAHASIANYA!!! SEMBUNYIKAN FILE BIAR GAK KETAHUAN | Steganografi](https://youtu.be/lQseW1pwLS4?si=sp_4cgdAuzzED5rw)  
> - [Belajar Osint #7: Photo Investigation Using Steghide](https://youtu.be/TYF_FcXH-7Q?si=opSi3LX99u1z05yU)  
> - [ILUSTRASI - Cara H4ck3r Mengirim Pesan Tersembunyi | Steganografi](https://youtu.be/529reqHpkcM?si=9lm5tHeHhAcp4cRQ)

## Fitur

1. **Dictionary Attack**:  
   Menggunakan teknik serangan kamus untuk meng-crack file stego yang dihasilkan oleh Steghide.
2. **Antarmuka Pengguna yang Sederhana**:  
   Menyediakan antarmuka berbasis teks yang mudah digunakan dengan instruksi yang jelas.
3. **Pemeriksaan Sistem**:  
   Memeriksa sistem operasi dan memastikan bahwa perangkat lunak yang diperlukan (seperti Steghide dan Binutils) terinstal sebelum melanjutkan.
4. **Validasi File**:  
   Memastikan bahwa file stego dan file wordlist yang dimasukkan oleh pengguna ada dan memiliki format yang benar.
5. **Penanganan Kesalahan yang Baik**:  
   Menangani berbagai kemungkinan kesalahan, seperti interupsi pengguna dan kesalahan sistem, dengan memberikan umpan balik yang informatif.

## Instalasi

Cara menginstal CrackStego ada [di sini](https://github.com/fixploit03/CrackStego/blob/main/INSTAL.md).

## Demonstrasi

Video demonstrasi CrackStego ada [di sini](https://youtu.be/PFvE8eLsRhk?si=h6Trq-w8bLOB1Jh8).

## Lisensi 

Program ini dilisensikan di bawah [Lisensi MIT](https://github.com/fixploit03/CrackStego/blob/main/LICENSE).

## Laporan Bug

Jika Anda menemukan bug atau masalah dalam program ini, silakan laporkan melalui [Issues](https://github.com/fixploit03/CrackStego/issues) di repositori GitHub. Sertakan deskripsi yang jelas mengenai masalah yang Anda temui.

> **Catatan**: Program ini hanya berfungsi untuk file stego yang dihasilkan oleh Steghide.
