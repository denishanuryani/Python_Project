total = 0
pesanan = []
harga = []

while True:
    print("""Daftar Makanan \n
        1. Chicken Burger Duluxe 37000
        2. Chicken Burger \t 33000
        3. Mc Spicy \t \t 44000
        4. McChicken \t \t 37000
        5. McNuggets \t \t 36000
        6. Chicken Snack Wrap \t 30000
        7. Spicy Chicken Bites \t 35000
        8. Chicken Finger \t 33000
        """)
    
    kode = int(input("Masukkan kode makanan :"))
    if kode == 1:
            pesanan.append("Chicken Burger Duluxe ")
            harga.append(37000)
            total += 37000
    elif kode == 2:
            pesanan.append("Chicken Burger")
            harga.append(33000)
            total += 33000
    elif kode == 3:
            pesanan.append("McSpicy ")
            harga.append(44000)
            total += 44000
    elif kode == 4:
            pesanan.append(" McChicken")
            harga.append(37000)
            total += 37000
    elif kode == 5:
            pesanan.append(" McNuggets")
            harga.append(36000)
            total += 36000
    elif kode == 6:
            pesanan.append("Chicken Snack Wrap")
            harga.append(30000)
            total += 30000
    elif kode == 7:
            pesanan.append("Spicy Chicken Bites")
            harga.append(35000)
            total += 35000
    elif kode == 8:
            pesanan.append("Chicken Finger")
            harga.append(33000)
            total += 33000
    else:
            print("Kode yang dimasukkan tidak valid.")


    lanjut = input("Lanjut Memesan? (y/t)")
    if lanjut == "t":
            print("")
            break
    
print('Makanan yang dipesan :', pesanan)
print('Harga makanan : ', harga)
print('Total yang harus dibayar :', total, '\n')

uang = int(input("Masukkan uang pembayaran :"))
if uang > total:
    print("Kembalian :", uang - total)
elif uang == total:
    print("Uang pas")
else:
    print("Uangnya kurang", uang - total)

    
