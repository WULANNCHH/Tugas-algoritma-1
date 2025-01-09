class Pegawai:
    def _init_(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

class PegawaiTetap(Pegawai):
    def _init_(self, nama, gaji_pokok, durasi_lembur):
        super()._init_(nama, gaji_pokok)
        self.tunjangan = 0.7 * gaji_pokok
        self.durasi_lembur = durasi_lembur

    def hitung_gaji_bersih(self):
        lembur = self.durasi_lembur * (0.1 * self.gaji_pokok)
        return self.gaji_pokok + self.tunjangan + lembur

class PegawaiTidakTetap(Pegawai):
    def _init_(self, nama, gaji_pokok, durasi_lembur):
        super()._init_(nama, gaji_pokok)
        self.durasi_lembur = durasi_lembur

    def hitung_gaji_bersih(self):
        lembur = self.durasi_lembur * (0.05 * self.gaji_pokok)
        return self.gaji_pokok + lembur

# Contoh penggunaan
pegawai1 = PegawaiTetap("Andi", 5000000, 10)
pegawai2 = PegawaiTidakTetap("Budi", 3000000, 8)

print(f"Nama: {pegawai1.nama}")
print(f"Gaji Pokok: Rp{pegawai1.gaji_pokok:,}")
print(f"Tunjangan: Rp{pegawai1.tunjangan:,}")
print(f"Durasi Lembur: {pegawai1.durasi_lembur} jam")
print(f"Gaji Bersih: Rp{pegawai1.hitung_gaji_bersih():,}\n")

print(f"Nama: {pegawai2.nama}")
print(f"Gaji Pokok: Rp{pegawai2.gaji_pokok:,}")
print(f"Tunjangan: -")
print(f"Durasi Lembur: {pegawai2.durasi_lembur} jam")
print(f"Gaji Bersih: Rp{pegawai2.hitung_gaji_bersih():,}")