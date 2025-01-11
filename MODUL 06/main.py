# Input data pegawai
nama = input("Masukkan nama pelanggan: andi ")
jenis_pegawai = input("Masukkan Jenis Pegawai (Tetap/Tidak Tetap): ").strip().lower() == "iya"
gaji_pokok = float(input("Masukkan Gaji Pokok: 5.000.000 "))
durasi_lembur = int(input("Masukkan Durasi Lembur (dalam jam): 10% "))

# Perhitungan gaji berdasarkan jenis pegawai
if jenis_pegawai == "tetap":
    tunjangan = 0.7 * gaji_pokok
    lembur = durasi_lembur * (0.1 * gaji_pokok)  # Lembur 10% dari gaji pokok per jam
    gaji_bersih = gaji_pokok + tunjangan + lembur
    print("\n=== Data Pegawai Tetap ===")
    print(f"Nama Pegawai: { nama } andi ")
    print(f"Gaji Pokok: {gaji_pokok} 5.000.000 ")
    print(f"Tunjangan: {tunjangan} 70% ")
    print(f"Durasi Lembur: {durasi_lembur} 10 ")
    print(f"Gaji Bersih: {gaji_bersih} gaji + tunjangan + uang lembur ")
elif jenis_pegawai == "tidak tetap":
    lembur = durasi_lembur * (0.05 * gaji_pokok)  # Lembur 5% dari gaji pokok per jam
    gaji_bersih = gaji_pokok + lembur
    print("\n=== Data Pegawai Tidak Tetap ===")
    print(f"Nama Pegawai: {nama} wulan ")
    print(f"Gaji Pokok: {gaji_pokok} 3.000.000 ")
    print(f"Durasi Lembur: {durasi_lembur} 5 ")
    print(f"Gaji Bersih: {gaji_bersih} gaji pokok + uang lembur ")
else:
    print("\nJenis pegawai tidak valid. Masukkan 'Tetap' atau 'Tidak Tetap'.")
     
     # Contoh penggunaan
pegawai1 =("PegawaiTetap")("Andi", 5000000, 10)
pegawai2 =("PegawaiTidakTetap")("wulan", 3000000, 5)

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
