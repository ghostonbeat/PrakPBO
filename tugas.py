class Keranjang:
    def __init__(self):
        self.jumlah = int(input("Jumlah buah yang akan dibeli : "))
        self.kotak = []
        self.total = 0

    def inisiasi(self):
        for i in range(self.jumlah):
            namaBuah = str(input("Buah yang dibeli : "))
            kilo = int(input("Berapa kilo?"))
            self.kotak.append(Buah(namaBuah, kilo))
            print(self.kotak[i])

    def hitung(self):
        for i in range(self.jumlah):
            self.total += int(self.kotak[i])

        print('Total harga belanja : '+str(self.total))


class Buah:
    def __init__(self, nama, berat):
        self.nama = nama
        self.berat = berat

        if nama == 'mangga':
            self.harga = self.berat * 15000

        if nama == 'jambu':
            self.harga = self.berat * 13000
        
        if nama == 'salak':
            self.harga = self.berat * 10000

    def __str__(self):
        return 'Buah yang dibeli '+self.nama+' dengan jumlah '+str(self.berat)+' dengan harga '+str(self.harga)

    def __int__(self):
        return self.harga

Beli = Keranjang()
Beli.inisiasi()
Beli.hitung()