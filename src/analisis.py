# Modul Analisis Statistik dan Ketuntasan

def hitung_statistik(data_siswa):
    """
    Menghitung total siswa, rata-rata, nilai maksimum, dan minimum.
    Menangani edge case jika data_siswa kosong.
    """
    if not data_siswa:
        return {"total_siswa": 0, "rata_rata": 0.0, "maksimum": 0.0, "minimum": 0.0}

    nilai_list = [item["nilai"] for item in data_siswa]
    total_siswa = len(nilai_list)
    rata_rata = sum(nilai_list) / total_siswa
    maksimum = max(nilai_list)
    minimum = min(nilai_list)

    return {
        "total_siswa": total_siswa,
        "rata_rata": rata_rata,
        "maksimum": maksimum,
        "minimum": minimum
    }

def tentukan_ketuntasan(data_siswa, kkm=60.0):
    """
    Menghitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM.
    """
    tuntas = 0
    belum_tuntas = 0
    for item in data_siswa:
        if item["nilai"] >= kkm:
            tuntas += 1
        else:
            belum_tuntas += 1
    return {"tuntas": tuntas, "belum_tuntas": belum_tuntas}
