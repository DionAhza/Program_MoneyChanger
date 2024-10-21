import random

# dollar = 0

def konversi():
    kurs = {'dollar': 15000, 'euro': 17000, 'yen': 130, 'pound': 20000}
    
    money = input('Ingin mengubah dollar, rupiah, euro, yen, pound, atau random? ').lower()

    if money == 'random':
        money = random.choice(list(kurs.keys()))
        print(f"Mata uang yang dipilih secara acak adalah {money}")

    if money == 'rupiah':
        uang = int(input('Masukkan jumlah uang rupiah: '))
        for mata_uang, nilai_tukar in kurs.items():
            hasil = uang / nilai_tukar
            print(f"Rp. {uang:,} bernilai: {mata_uang.capitalize()} {hasil:.2f}")
    elif money in kurs:
        uang = int(input(f"Masukkan jumlah uang {money}: "))
        hasil = uang * kurs[money]
        print(f"{money.capitalize()} {uang:,} bernilai: Rp. {hasil:,}")
    else:  
        print("Mata uang tidak dikenali.")

while True:
    konversi()
    ulangi = input("Ingin melakukan konversi lagi? (ya/tidak): ").lower()
    if ulangi != 'ya':
        print("Terima kasih telah menggunakan program konversi!")
        break
