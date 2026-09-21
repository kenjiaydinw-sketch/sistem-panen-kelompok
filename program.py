def input_data():
    n = int(input("Masukkan jumlah lahan: "))
    return [float(input(f"Hasil panen lahan ke-{i+1} (kg): ")) for i in range(n)]

def buat_laporan(data):
    if not data:
        print("Belum ada data panen untuk dilaporkan.")
        return

    total = sum(data)
    rata_rata = total / len(data)
    tertinggi = max(data)
    terendah = min(data)

    print("=== LAPORAN HASIL PANEN ===")
    print(f"Total hasil panen   : {total} kg")
    print(f"Rata-rata per lahan : {rata_rata:.2f} kg")
    print(f"Hasil tertinggi     : {tertinggi} kg")
    print(f"Hasil terendah      : {terendah} kg")

if __name__ == "__main__":
    data = input_data()
    buat_laporan(data)
