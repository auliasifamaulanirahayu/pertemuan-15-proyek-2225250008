# Perancangan dan Dokumentasi Hasil Test Case

Dokumen ini mencatat pengujian sistem secara mendalam mencakup kondisi Normal, Boundary (Batas), Invalid, dan File Edge Case.

| ID | Kategori | Target Modul | Input / Kondisi | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|---|
| TC01 | Normal | `analisis.py` | Data `[85.0, 60.0, 90.0]` | Rata-rata: 78.33 | Rata-rata: 78.33 | PASS |
| TC02 | Batas Min | `utilitas.py` | Nilai `0` | `(True, 0.0)` | `(True, 0.0)` | PASS |
| TC03 | Batas Max | `utilitas.py` | Nilai `100` | `(True, 100.0)` | `(True, 100.0)` | PASS |
| TC04 | Invalid High | `utilitas.py` | Nilai `105` | `(False, None)` | `(False, None)` | PASS |
| TC05 | Invalid Type | `utilitas.py` | String `"abc"` | `(False, None)` | `(False, None)` | PASS |
| TC06 | Invalid File | `data_io.py` | File tidak ditemukan | Mengembalikan `[]` + Warning | Mengembalikan `[]` + Warning | PASS |
| TC07 | Batas KKM | `analisis.py` | Nilai `60` | Status: Tuntas | Status: Tuntas | PASS |
| TC08 | Bawah KKM | `analisis.py` | Nilai `59` | Status: Belum Tuntas | Status: Belum Tuntas | PASS |
| TC09 | Empty List | `analisis.py` | List kosong `[]` | Rata-rata 0.0 | Rata-rata 0.0 | PASS |
