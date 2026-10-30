# Modul Utilitas Validasi Data

def validasi_nilai(nilai_str):
    """
    Memvalidasi apakah nilai_str berupa angka float/int yang berada di rentang 0 - 100.
    Mengembalikan tuple (is_valid, float_val).
    """
    try:
        val = float(nilai_str)
        if 0 <= val <= 100:
            return True, val
        else:
            return False, None
    except ValueError:
        return False, None
