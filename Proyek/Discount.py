
print('\nDiskon Potongan Harga')
print('=======================')

totalBelanja = int(input('Masukkan Total Belanja : '))

if(totalBelanja > 500000) :
    diskon = 0.3
    print('Selmaat anda mendapatkan diskon 30%')
elif(totalBelanja > 250000) :
    diskon = 0.15
    print('Selamat anda mendapatkan diskon 15%')
elif(totalBelanja > 50000) :
    diskon = 0.05
    print('Selamat anda mendapatkan diskon 5%')
elif(totalBelanja < 50000):
    diskon = 0

totalBayar = totalBelanja - (totalBelanja * diskon)

print(f'Total Bayar = {totalBayar}')
print('=======================')

