def rata_rata(nilai):
    if nilai == []:
        return "Data kosong"
    total = sum(nilai)
    jumlah = len(nilai)
    return total / jumlah

data = [80, 75, 90, 60, 85]
print("Rata-rata =", rata_rata(data))
