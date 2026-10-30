# PROPOSAL PROYEK PROGRAM SEDERHANA
## Program Rekap dan Analisis Nilai Matematika Kelas

**Penyusun:** Aulia Sifa Maulani Rahayu (NIM: 2225250008 / Kelas 3A)  
**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Pendidikan Matematika, FKIP Untirta  
**Tahun Ajaran:** 2026/2027 Ganjil  

---

### 1. Judul Proyek
**Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Terminal Python**

### 2. Latar Belakang
Guru matematika di sekolah sering kali menghabiskan banyak waktu secara manual untuk merekap nilai ujian siswa, mengkalkulasi statistik dasar (rata-rata, nilai tertinggi, dan nilai terendah), serta mengevaluasi jumlah siswa yang tuntas Kriteria Ketuntasan Minimal (KKM). Proses manual berisiko mengalami kesalahan hitung (*human error*) dan tidak efisien. Oleh karena itu, dibutuhkan sebuah program konsol/terminal sederhana menggunakan Python yang mampu membaca file data nilai, memvalidasi isi data, menghitung statistik secara presisi, dan menyimpan laporan analisis ke dalam file teks secara otomatis.

### 3. Pengguna dan Tujuan
* **Pengguna Utama:** Guru Matematika / Pengajar.
* **Tujuan:** 
  1. Mempermudah dan mempercepat proses pengolahan data nilai kelas.
  2. Meminimalisir kesalahan perhitungan statistik dan penentuan ketuntasan belajar.
  3. Menyediakan laporan ringkasan yang terekap secara rapi dalam format file `.txt`.

### 4. Ruang Lingkup & Batasan Proyek
* **Fitur Wajib (Core Features):**
  1. Membaca data nilai dari file teks (`data/nilai_contoh.txt`).
  2. Memvalidasi rentang nilai (harus berupa angka 0 - 100) dan menangani error data tidak valid.
  3. Menghitung nilai rata-rata, nilai maksimum (tertinggi), dan nilai minimum (terendah).
  4. Menghitung jumlah serta persentase siswa yang tuntas/belum tuntas berdasarkan KKM (KKM = 60).
  5. Menulis dan menyimpan hasil rekapitulasi ke file laporan (`output/laporan_rekap.txt`).
* **Batasan Proyek:**
  * Program berbasis Terminal / Console (tanpa GUI).
  * Format input file sederhana berupa teks per baris `NIM,Nama,Nilai`.

### 5. Kebutuhan Fungsional
* **F01:** Program dapat membaca file data nilai siswa.
* **F02:** Program dapat memvalidasi rentang nilai (0–100) dan mengabaikan/memberikan peringatan pada data invalid.
* **F03:** Program dapat menghitung statistik (rata-rata, min, max).
* **F04:** Program dapat mengklasifikasikan ketuntasan siswa berdasarkan KKM (default = 60).
* **F05:** Program dapat mengeksport laporan ke file output.

### 6. Spesifikasi Input, Proses, dan Output (IPO)
* **Input:** File `data/nilai_contoh.txt` berisi record siswa dengan format `NIM,Nama,Nilai`.
* **Proses:** Membaca baris, memvalidasi data, menghitung statistik, dan mengelompokkan ketuntasan KKM.
* **Output:** Tampilan ringkasan di terminal dan file `output/laporan_rekap.txt`.

### 7. Pemilihan Struktur Data
* `list of dict`: Menyimpan data record siswa `[{"nim": "A001", "nama": "Ayu", "nilai": 85.0}, ...]`.
* `dict`: Menyimpan ringkasan statistik dan ketuntasan.

### 8. Pembagian Tugas (Mandiri)
* **PIC Penanggung Jawab:** Aulia Sifa Maulani Rahayu (100% Kontribusi Individu).

### 9. URL Repositori GitHub
`https://github.com/aaliasifa/pertemuan-15-proyek-2225250008`
