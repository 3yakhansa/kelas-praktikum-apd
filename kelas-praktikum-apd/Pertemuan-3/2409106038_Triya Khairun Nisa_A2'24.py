print("""
      ===========================================
      Kalkulator Sederhana
      1. +
      2. -
      3. *
      4. /
      ===========================================
      """)

fitur = int(input("pilih fitur : "))
match fitur :
     case 1:
         a = int(input("Masukkan angka 1 : "))
         b = int(input("Masukkan angka 2 : "))
         c = a + b 
         print (f"hasil penjumlahan angka 1 dan angka 2 adalah {c}")
     case 2:
         a = int(input("Masukkan angka 1 : "))
         b = int(input("Masukkan angka 2 : "))
         c = a - b 
         print (f"hasil pengurangan angka 1 dan angka 2 adalah {c}")
     case 3:
         a = int(input("Masukkan angka 1 : "))
         b = int(input("Masukkan angka 2 : "))
         c = a * b 
         print (f"hasil perkalian angka 1 dan angka 2 adalah {c}")
     case 4:
         a = int(input("Masukkan angka 1 : "))
         b = int(input("Masukkan angka 2 : "))
         c = a / b 
         print (f"hasil pembagian angka 1 dan angka 2 adalah {c}")
     case _:
        print("Tidak Valid")
      

gender = input("Masukkan jenis kelamin [P/W]: ")
result = "Pria" if gender == "P" else "Wanita" if gender == "W" else "Tidak Diketahui"
print("Jenis Kelamin adalah",result)

buku = int(input("Masukkan jumlah buku = "))
harga = int(input("Masukkan total harga buku = "))
diskon = 0.20
total_harga = buku * harga


if buku >= 5 and total_harga > 100000:
     total_setelah = total_harga * diskon
     total_akhir = total_harga - total_setelah
     print(f"diskon yang diterima sebanyak {total_setelah:.0f}")
     print(f"Anda harus membayar sebanyak {total_akhir:.0f} setelah mendapat diskon 20%")
else: print("anda tidak mendapat diskon")

nilai = int(input("Masukkan Nilai: "))

if nilai > 100 :
    print("kondisi tidak memenuhi syarat")
if nilai >= 80 : 
    if nilai >= 90 and nilai <= 100 :
        print("Nilai Anda A+")
    if nilai >= 80 and nilai <= 89 :
        print("Nilai Anda A-")
if nilai >= 70 : 
    if nilai >= 75 and nilai <= 79 :
        print("Nilai Anda B+")
    if nilai >= 70 and nilai <= 74 :
        print("Nilai Anda B-")
else :
    print("kondisi tidak memenuhi syarat")
    
