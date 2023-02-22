p = input(" masukkan plat nomor: ").upper().split(" ")

 
if  p[1] >= 0 and p[1]<= 3000:
    print("Plat Nomor Tersebut Diperuntukkan untuk Mobil")
elif p[1] >3000 and p[1]<= 4000:
    print("Plat Nomor Tersebut diperuntukan untuk Motor")
elif p[1] >4000 and p[1]<= 5000: 
    print("Plat Nomor Tersebut Diperuntukan untuk Angkutan Umum")
else:
    print("plat nomor tidak teridentifikasi")
    