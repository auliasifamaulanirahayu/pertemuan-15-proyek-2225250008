# Entry Point Utama Program Rekap Nilai

import os
from data_io import baca_file_nilai, simpan_laporan
from analisis import hitung_statistik, tentukan_ketuntasan

def main():
    print("==================================================")
    print("   PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA   ")
    print("==================================================")
    
    # Path relatif file input
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(base_dir, "data", "nilai_contoh.txt")
    
    print(f"
[1] Membaca data dari: {filepath}")
    data_siswa = baca_file_nilai(filepath)
    
    if not data_siswa:
        print("[ERROR] Tidak ada data valid untuk diproses.")
        return

    print("
[2] Menghitung Statistik Kelas & Status KKM...")
    stats = hitung_statistik(data_siswa)
    ketuntasan = tentukan_ketuntasan(data_siswa, kkm=60.0)

    print("
=== HASIL REKAPITULASI KELAS ===")
    print(f"Total Siswa Valid  : {stats['total_siswa']} orang")
    print(f"Rata-rata Kelas     : {stats['rata_rata']:.2f}")
    print(f"Nilai Tertinggi     : {stats['maksimum']}")
    print(f"Nilai Terendah      : {stats['minimum']}")
    print(f"Siswa Tuntas (>=60) : {ketuntasan['tuntas']} orang")
    print(f"Siswa Belum Tuntas  : {ketuntasan['belum_tuntas']} orang")

    output_path = os.path.join(base_dir, "output", "laporan_rekap.txt")
    print(f"
[3] Menyimpan Laporan ke File...")
    simpan_laporan(stats, ketuntasan, output_path)
    print("
[SELESAI] Eksekusi program berhasil dijalankan tanpa error.")

if __name__ == "__main__":
    main()
