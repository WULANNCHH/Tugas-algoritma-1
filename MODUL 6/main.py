class pegawai
def_init_(self,nama,gaji_pokok):
self.nama = nama
self.gaji_pokok = gaji_pokok

class pegawai tetap(pegawai):
def_init_(self,nama,gaji_pokok,durasi_lembur):
super()._init_(nama,gaji_pokok)
self.tunjangan = 0.7 * gaji_pokok
self.durasi_lembur = durasi_lembur

def hitung_gaji_bersih(self):
lembur = self.durasi_lembur * (0.1 * self.gaji_pokok)
return self.gaji_pokok + self.tunjangan + lembur

class pegawai tidak tetap(pegawai):
def_init_(self,nama,gaji_pokok,durasi_lembur):
super()._init_(nama,gaji_pokok)
self.durasi_lembur = durasi_lembur

def hitung_gaji_bersih(self):
lembur = self.durasi_lembur * (0.05 * self.gaji_pokok)
return self.gaji_pokok + lembur

# contoh penggunaan
pegawai1 = pegawai tetap("andi",5000000,10)
pegawai2 = pegawai tidak tetap("budi",4000000,8)
