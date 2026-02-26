# Latihan

class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis

    def sound(self):
        return "suara"

class Mobil(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, bahan_bakar):
        super().__init__(jenis, merk, tahun_rilis)
        self.__bahan_bakar = bahan_bakar

class Motor(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, speed):
        super().__init__(jenis, merk, tahun_rilis)
        self.__speed = speed

kendaraan1 = Vehicle("Tayo", "Generic", 2020)
mobil2 = Mobil("mobil", "Toyota", 2022, "Bensin")
motor2 = Motor("motor", "RGP26", 2026, "1000cc")

print(kendaraan1.jenis, kendaraan1.merk, kendaraan1.tahun_rilis, kendaraan1.sound())
print(mobil2.jenis, mobil2.merk, mobil2.tahun_rilis, mobil2.sound())
print(motor2.jenis, motor2.merk, motor2.tahun_rilis, motor2.sound())