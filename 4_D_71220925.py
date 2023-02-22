nama = input("Masukkan Nama Lengkap Anda:")
jurusan = input("Masukkan Prodi Anda:")
nilai= input("Masukkan Nilai (dalam huruf) yang anda dapat:").upper()
nilaia =4.0
nilaia1 = 3.75
nilaib1 = 3.25
nilaib2 = 3.0
nilaib3= 2.75
nilaic1= 2.25
nilaic2 = 2.0
nilaid = 1.0
nilaie = 0 

#try: 
if nilai == "A":
        print("Nilai anda adalah", nilaia,"wihhh kerenn")
elif nilai == "A-":
        print(" Nilai anda adalah",nilaia1," keren")
elif nilai == "B+":
        print("Nilai Anda adalah", nilaib1,"masi aman")
elif nilai == "B-":
        print("Nilai anda adalah", nilaib2," eits")
elif nilai == "C+":
        print("Nilai Anda adalah", nilaic1," yokk smangat")
elif nilai == "C":
        print(" Nilai Anda adalah", nilaic2, "belajar yok")
elif nilai == "D":
        print("Nilai anda adalah", nilaid, "belajar yang giat")
elif nilai == "E":
        print("Nilai anda adalah", nilaie, " lebih giat lagi belajarnya")
else:
        print("Nilai yang anda masukkan tidak Valid")