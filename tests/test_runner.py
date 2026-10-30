# Skrip Automation Testing (Test Suite)
import sys
import os

# Menambahkan folder src ke sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utilitas import validasi_nilai
from analisis import hitung_statistik, tentukan_ketuntasan

def test_suite():
    print("=== MENJALANKAN AUTOMATION TEST SUITE ===")
    
    # TC01: Normal
    data_test = [{"nilai": 85.0}, {"nilai": 60.0}, {"nilai": 90.0}]
    stats = hitung_statistik(data_test)
    assert round(stats["rata_rata"], 2) == 78.33, "TC01 Gagal!"
    print("[PASS] TC01: Rata-rata data normal")

    # TC02 & TC03: Batas 0 & 100
    assert validasi_nilai("0") == (True, 0.0), "TC02 Gagal!"
    assert validasi_nilai("100") == (True, 100.0), "TC03 Gagal!"
    print("[PASS] TC02 & TC03: Validasi batas 0 dan 100")

    # TC04 & TC05: Invalid 105 & 'abc'
    assert validasi_nilai("105") == (False, None), "TC04 Gagal!"
    assert validasi_nilai("abc") == (False, None), "TC05 Gagal!"
    print("[PASS] TC04 & TC05: Validasi data invalid (105 & 'abc')")

    # TC07 & TC08: Batas KKM 60 vs 59
    kunt_60 = tentukan_ketuntasan([{"nilai": 60.0}], kkm=60.0)
    kunt_59 = tentukan_ketuntasan([{"nilai": 59.0}], kkm=60.0)
    assert kunt_60["tuntas"] == 1, "TC07 Gagal!"
    assert kunt_59["belum_tuntas"] == 1, "TC08 Gagal!"
    print("[PASS] TC07 & TC08: Ketuntasan KKM 60 dan 59")

    # TC09: List kosong
    stats_empty = hitung_statistik([])
    assert stats_empty["rata_rata"] == 0.0, "TC09 Gagal!"
    print("[PASS] TC09: Penanganan list kosong (ZeroDivisionError protection)")

    print("
[SELAMAT] Seluruh Test Case Berhasil Lulus (100% PASS)!")

if __name__ == "__main__":
    test_suite()
