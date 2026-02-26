try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

    hasil = angka1 / angka2
    print("Hasil pembagian:", hasil)

except ValueError:
    print("Terjadi kesalahan: input harus berupa angka.")

except ZeroDivisionError:
    print("Terjadi kesalahan: tidak boleh membagi dengan nol.")

finally:
    print("Program selesai.")

    