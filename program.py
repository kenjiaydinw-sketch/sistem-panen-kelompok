def input_data():
    n = int(input("Masukkan jumlah lahan: "))
    return [float(input(f"Hasil panen lahan ke-{i+1} (kg): ")) for i in range(n)]

def buat_laporan(data):
    if not data:
        print("Belum ada data hasil panen.")
        return

    total = sum(data)
    rata_rata = total / len(data)
    hasil_tertinggi = max(data)
    hasil_terendah = min(data)

    print("\nLaporan hasil panen")
    print(f"Total hasil panen: {total:.2f} kg")
    print(f"Rata-rata per lahan: {rata_rata:.2f} kg")
    print(f"Hasil panen tertinggi: {hasil_tertinggi:.2f} kg")
    print(f"Hasil panen terendah: {hasil_terendah:.2f} kg")

if __name__ == "__main__":
    data = input_data()
    buat_laporan(data)
