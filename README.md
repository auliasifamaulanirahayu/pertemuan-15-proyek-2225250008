# Program Rekap dan Analisis Nilai Matematika Kelas

**Nama:** Aulia Sifa Maulani Rahayu  
**NIM:** 2225250008  
**Kelas:** 3A  
**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Pendidikan Matematika, FKIP Universitas Sultan Ageng Tirtayasa  
**Dosen Pengampu:** Dr. Aan Hendrayana, S.Si., M.Pd.  

---

## Deskripsi
Program ini adalah aplikasi konsol berbasis Python yang dirancang untuk membantu guru matematika dalam mengolah dan menganalisis data nilai siswa secara efisien dan akurat. Program membaca data nilai dari file teks, memvalidasi input data (mencegah data salah/di luar rentang 0–100), menghitung statistik kelas (rata-rata, nilai tertinggi, nilai terendah), menentukan ketuntasan belajar berdasarkan KKM (KKM = 60), serta menghasilkan file laporan rekapitulasi otomatis.

---

## Fitur Utama
1. **Pembacaan File Data (`data_io.py`)**: Membaca record nilai dari file teks `data/nilai_contoh.txt`.
2. **Validasi Input Terisolasi (`utilitas.py`)**: Memvalidasi rentang nilai (0–100) dan menangani exception input non-numerik (`ValueError`).
3. **Analisis Statistik & Ketuntasan (`analisis.py`)**: Menghitung rata-rata, nilai maksimum, nilai minimum, serta jumlah & persentase siswa tuntas/belum tuntas KKM.
4. **Ekspor Laporan Otomatis**: Menyimpan hasil rekapitulasi secara rapi ke file `output/laporan_rekap.txt`.
5. **Pengujian Terintegrasi & Assert**: Memiliki skrip pengetesan otomatis (`tests/test_runner.py`) untuk pengujian regresi (*regression test*).

---

## Persyaratan System
* Python 3.8 atau versi yang lebih baru.
* Visual Studio Code (disarankan) atau Terminal/CLI standar.

---

## Cara Menjalankan Program Utama
1. Buka terminal di VS Code pada root folder proyek.
2. Jalankan perintah berikut:
   ```bash
   python3 src/main.py
   ```

## Cara Menjalankan Test Case Automasi
Untuk memverifikasi bahwa seluruh modul dan fungsi berjalan tanpa error (PASS):
```bash
python3 tests/test_runner.py
```

---

## Struktur Folder Proyek
```text
pertemuan-15-proyek-2225250008/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   ├── test_case.md
│   └── test_runner.py
├── docs/
│   └── bug_log.md
└── output/
    ├── .gitkeep
    └── laporan_rekap.txt
```

---

## Hasil Pengujian (Test Case Matrix)

| ID | Fitur Target | Input / Kondisi | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Rata-rata | `[85.0, 60.0, 90.0]` | `78.33` | `78.33` | **PASS** |
| TC02 | Batas Nilai Minimal | `0.0` | Diterima sebagai nilai valid | `(True, 0.0)` | **PASS** |
| TC03 | Batas Nilai Maksimal | `100.0` | Diterima sebagai nilai valid | `(True, 100.0)` | **PASS** |
| TC04 | Nilai Invalid (Di Luar Rentang) | `105.0` | Ditolak `(False, None)` | `(False, None)` | **PASS** |
| TC05 | Input Non-Numerik | `"abc"` | Ditolak dengan `ValueError` ditangani | `(False, None)` | **PASS** |
| TC06 | File Tidak Ditemukan | `"file_palsu.txt"` | `FileNotFoundError` ditangani | Pesan warning & mengembalikan `[]` | **PASS** |
| TC07 | Batas Ketuntasan KKM | `60.0` | Status: Tuntas | Tuntas | **PASS** |
| TC08 | Di Bawah KKM | `59.0` | Status: Belum Tuntas | Belum Tuntas | **PASS** |
| TC09 | Data Kosong | `[]` | Rata-rata: 0.0, Tuntas: 0 | `total_siswa = 0` | **PASS** |

---

## Known Issues & Log Perbaikan Bug
Detail bug log tercantum pada file `docs/bug_log.md`.
* **BUG-01 (Closed)**: `ZeroDivisionError` pada perhitungan rata-rata list kosong $
ightarrow$ Telah diperbaiki dengan validasi `if not data_siswa`.
* **BUG-02 (Closed)**: `ValueError` saat membaca baris berisi karakter non-numerik $
ightarrow$ Telah diperbaiki pada modul `utilitas.py`.

---

## Anggota dan Kontribusi
* **Aulia Sifa Maulani Rahayu (NIM: 2225250008)**: Penanggung jawab tunggal (Pengerjaan Mandiri Proyek Akhir) — Merancang proposal, mengimplementasikan fungsi Python, menyusun test runner, menguji bug, dan menyusun dokumentasi.

---

## Referensi / Bantuan
1. Hendrayana, A. (2026). *Bahan Ajar Pertemuan 14 & 15 Algoritma dan Pemrograman: Perancangan, Implementasi, Pengujian, dan Dokumentasi Proyek*. Untirta.
2. Python Software Foundation. *Python 3 Documentation - Exception Handling & File I/O*.

