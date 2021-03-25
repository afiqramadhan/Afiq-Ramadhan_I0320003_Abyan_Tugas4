# menghitung berat bagasi penumpang
lbs = 50
berat_maksimum = lbs * 0.454
print("Berat maksimum bagasi penumpang adalah", berat_maksimum, "Kg")

# memasukkan nilai berat bagasi penumpang
berat_bawaan = float(input("Berat barang bawaan penumpang : "))

# proses analisis data
if berat_bawaan <= berat_maksimum:
    status_barang = True
    print("status barang: ",status_barang)
else:
    status_barang = False
    print("status barang : ", status_barang)

if not status_barang:
    print("Anda dikenakan pajak")
else:
    print("Anda tidak dikenakan pajak")
