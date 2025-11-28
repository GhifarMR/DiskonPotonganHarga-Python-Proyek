
print('\nDiskon Potongan Harga')
print('=======================')

totalBelanja = int(input('Masukkan Total Belanja : '))

if(totalBelanja > 500000) :
    diskon = 30
elif(totalBelanja > 250000) :
    diskon = 15
elif(totalBelanja > 50000) :
    diskon = 5
else:
    diskon = 0

print(f'Selamat anda mendapatkan diskon {diskon}%')
totalBayar = totalBelanja - (totalBelanja * (diskon / 100))

print(f'Total Bayar = {totalBayar}')
print('=======================')
