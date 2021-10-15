class MesinGabut():
    def __init__(self, biner):
        self.biner = biner
        self.role = ['q1', 'q2', 'q3']
        self.curr = self.role[0]
        self.masuk = False

    def circle(self, binchar):
        if self.curr == self.role[0]:
            if binchar == '0':
                self.curr = self.role[1]
                self.masuk = False
            if binchar == '1':
                self.curr = self.role[2]
                self.masuk = True
            
        if self.curr == self.role[1]:
            if binchar == '0' or binchar == '1':
                pass

    def cek(self, curr, jum):
        if curr < jum:
            if self.biner[curr] != '0' or self.biner != '1':
                return False
            else:
                return self.cek(curr+1, jum)
        else:
            return True

if __name__ == '__main__':
    ambil = input()
    mesin = MesinGabut(ambil)

    if cek(0, len(mesin.biner)):
        print("Sesuai Kriteria")
    else:
        print("Tidak Sesuai Kriteria")