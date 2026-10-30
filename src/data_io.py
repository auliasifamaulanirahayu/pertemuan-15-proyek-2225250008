# Modul Input/Output Data File

import os
from utilitas import validasi_nilai

def baca_file_nilai(filepath):
    """
    Membaca file data nilai dengan format NIM,Nama,Nilai.
    """
    data_valid = []
    if not os.path.exists(filepath):
        print(f"[WARNING] File '{filepath}' tidak ditemukan! Mengembalikan data kosong.")
        return data_valid

    with open(filepath, 'r', encoding='utf-8') as file:
        for idx, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) == 3:
                nim, nama, nilai_str = parts[0].strip(), parts[1].strip(), parts[2].strip()
                is_valid, val = validasi_nilai(nilai_str)
                if is_valid:
                    data_valid.append({"nim": nim, "nama": nama, "nilai": val})
                else:
                    print(f"[LOG VALIDASI] Baris {idx} diabaikan (Nilai '{nilai_str}' di luar rentang 0-100 / invalid).")
            else:
                print(f"[LOG VALIDASI] Baris {idx} diabaikan (Format kolom tidak sesuai).")
    return data_valid

def simpan_laporan(statistik, ketuntasan, filepath_output):
    """
    Menulis hasil analisis ke file teks output.
    """
    os.makedirs(os.path.dirname(filepath_output), exist_ok=True)
    with open(filepath_output, 'w', encoding='utf-8') as file:
        file.write("============================================
")
        file.write("   LAPORAN REKAPITULASI NILAI MATEMATIKA    
")
        file.write("============================================

")
        file.write(f"Jumlah Siswa Valid : {statistik.get('total_siswa', 0)} orang
")
        file.write(f"Rata-rata Kelas    : {statistik.get('rata_rata', 0):.2f}
")
        file.write(f"Nilai Tertinggi    : {statistik.get('maksimum', 0)}
")
        file.write(f"Nilai Terendah     : {statistik.get('minimum', 0)}
")
        file.write("--------------------------------------------
")
        file.write(f"Siswa Tuntas (>=60): {ketuntasan.get('tuntas', 0)} orang
")
        file.write(f"Siswa Belum Tuntas : {ketuntasan.get('belum_tuntas', 0)} orang
")
        file.write("============================================
")
    print(f"[INFO] Laporan berhasil disimpan ke '{filepath_output}'.")
