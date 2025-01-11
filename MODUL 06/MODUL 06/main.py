# Input data pegawai
nama = input("Masukkan Nama Pegawai: ")
jenis_pegawai = input("Masukkan Jenis Pegawai (Tetap/Tidak Tetap): ").lower()
gaji_pokok = float(input("Masukkan Gaji Pokok: "))
durasi_lembur = int(input("Masukkan Durasi Lembur (dalam jam): "))

# Perhitungan gaji berdasarkan jenis pegawai
if jenis_pegawai == "tetap":
    tunjangan = 0.7 * gaji_pokok
    lembur = durasi_lembur * (0.1 * gaji_pokok)  # Lembur 10% dari gaji pokok per jam
    gaji_bersih = gaji_pokok + tunjangan + lembur
    print("\n=== Data Pegawai Tetap ===")
    print(f"Nama Pegawai: {nama}")
    print(f"Gaji Pokok: {gaji_pokok}")
    print(f"Tunjangan: {tunjangan}")
    print(f"Durasi Lembur: {durasi_lembur} jam")
    print(f"Gaji Bersih: {gaji_bersih}")
elif jenis_pegawai == "tidak tetap":
    lembur = durasi_lembur * (0.05 * gaji_pokok)  # Lembur 5% dari gaji pokok per jam
    gaji_bersih = gaji_pokok + lembur
    print("\n=== Data Pegawai Tidak Tetap ===")
    print(f"Nama Pegawai: {nama}")
    print(f"Gaji Pokok: {gaji_pokok}")
    print(f"Durasi Lembur: {durasi_lembur} jam")
    print(f"Gaji Bersih: {gaji_bersih}")
else:
    print("\nJenis pegawai tidak valid. Masukkan 'Tetap' atau 'Tidak Tetap'.")