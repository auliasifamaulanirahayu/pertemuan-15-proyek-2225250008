# Documentasi Bug Log & Tracking Perbaikan

Berikut adalah catatan perbaikan bug (*bug tracking log*) selama tahapan implementasi Pertemuan 15:

| Bug ID | Gejala Error | Akar Penyebab | Perbaikan yang Dilakukan | Status |
|---|---|---|---|---|
| BUG-01 | `ZeroDivisionError` saat input data kosong | Fungsi `hitung_rata_rata()` membagi `sum(nilai)` dengan `len(nilai)` tanpa mengecek apakah `len(nilai) == 0`. | Menambahkan validasi `if not data_siswa: return {"total_siswa": 0, "rata_rata": 0.0, ...}` pada `analisis.py`. | **Closed** |
| BUG-02 | `ValueError` saat membaca data non-numerik (misal `"abc"`) | Konversi langsung `float(nilai_str)` memicu kram exception. | Menambahkan penanganan `try-except ValueError` di `utilitas.py` dan mengembalikan `(False, None)`. | **Closed** |
| BUG-03 | Penumpukan data pada file laporan | Penulisan laporan menggunakan mode append tanpa pembersihan. | Dipastikan menggunakan mode `'w'` (write) agar laporan yang dihasilkan selalu yang terbaru. | **Closed** |
