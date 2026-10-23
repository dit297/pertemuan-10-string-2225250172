# Pertemuan 10 String dan Pengolahan Teks

Nama: Aditya Setianugroho  
NIM: 2225250172  
Kelas: 3F

## Tujuan

Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan

Pastikan Anda berada di direktori pertemuan-10-string-NIM.

Jalankan file tugas menggunakan perintah berikut di terminal:

```bash
python tugas/normalisasi_data_mahasiswa.py
```

## Algoritma

Proses normalisasi data mahasiswa dilakukan dengan langkah-langkah berikut:

1. Program akan meminta pengguna memasukkan (input) nama lengkap dan kode kelas dalam bentuk string.
2. Normalisasi nama dilakukan dengan metode strip() untuk menghapus kelebihan spasi di awal dan akhir, serta metode title() untuk mengubah awalan setiap kata menjadi huruf kapital.
3. String nama yang telah dinormalisasi dipecah menjadi list kata menggunakan metode split().
4. Inisial dibentuk dengan mengambil karakter pertama (indeks 0) dari setiap kata yang telah dipecah tadi dan digabungkan kembali.
5. Normalisasi kode kelas menggunakan kombinasi beberapa metode: strip() untuk menghapus spasi di ujung teks, upper() untuk menjadikannya huruf kapital semua, split() untuk memecahnya jika ada spasi di tengah, lalu digabungkan kembali menggunakan join() dengan separator tanda hubung (-).
6. Terakhir, program mencetak nama bersih, kode kelas yang sudah diformat, jumlah kata dari nama, serta inisial yang dihasilkan ke layar.

## Test Case

| Input Nama | Input Kode | Hasil yang Diharapkan (Nama \| Kode \| Inisial) | Hasil Aktual | Status |
|---|---|---|---|---|
| aan hendrayana | pmat a 2026 | Aan Hendrayana<br>PMAT-A-2026<br>AH | Aan Hendrayana<br>PMAT-A-2026<br>AH | Berhasil |
| fATHIYYAH MUTHMAINNAH | kelas b | Fathiyyah Muthmainnah<br>KELAS-B<br>FM | Fathiyyah Muthmainnah<br>KELAS-B<br>FM | Berhasil |
| BUDI | pmtk 01 | Budi<br>PMTK-01<br>B | Budi<br>PMTK-01<br>B | Berhasil |
| siti nur aisyah | kelas c | Siti Nur Aisyah<br>KELAS-C<br>SNA | Siti Nur Aisyah<br>KELAS-C<br>SNA | Berhasil |

## Refleksi

Satu masalah teks yang ditemukan adalah adanya spasi ganda atau format huruf yang acak-acakan saat pengguna memasukkan data, yang bisa menyebabkan kegagalan saat dilakukan perbandingan data nantinya. Cara memperbaikinya adalah dengan melakukan pembersihan teks, pertama-tama memakai strip() untuk menghilangkan spasi kosong di batas teks, lalu menggunakan kombinasi split() dan join() untuk merapikan spasi berlebih di tengah-tengah. Setelah spasinya teratur, penggunaan upper(), lower(), atau title() ditambahkan untuk menyeragamkan kapitalisasinya menjadi sebuah bentuk baku.
