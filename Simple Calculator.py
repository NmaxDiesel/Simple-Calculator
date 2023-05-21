def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

def kalkulator():
    print("=== KALKULATOR ===")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    pilihan = input("Masukkan nomor operasi (1/2/3/4): ")

    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        hasil = tambah(num1, num2)
        print(f"Hasil: {hasil}")
    elif pilihan == '2':
        hasil = kurang(num1, num2)
        print(f"Hasil: {hasil}")
    elif pilihan == '3':
        hasil = kali(num1, num2)
        print(f"Hasil: {hasil}")
    elif pilihan == '4':
        hasil = bagi(num1, num2)
        print(f"Hasil: {hasil}")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

kalkulator()
