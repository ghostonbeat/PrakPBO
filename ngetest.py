class wow():
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def cetak(self):
        print(self.tambah())
        print(self.kurang())
        print(self.kali())
        print(self.bagi())


    def tambah(self):
        return self.A+self.B

    def kurang(self):
        return self.A-self.B

    def kali(self):
        return self.A*self.B

    def bagi(self):
        return self.A/self.B

if __name__ == '__main__':
    calc = wow(5, 2)
    calc.cetak()