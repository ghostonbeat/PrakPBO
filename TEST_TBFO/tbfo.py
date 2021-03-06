class MesinGabut():
    def __init__(self, biner):
        self.biner = []
        for i in range(len(biner)):
            self.biner.append(biner[i])

        """Inisiasi formasi (cek aja alurnya di tbfo.drawio.png)"""
        self.role = ['q1', 'q2', 'q3']
        self.curr = self.role[0]

    def circle(self, start, finish, tentu):
        if start < finish:
            if self.curr == self.role[0]:
                if self.biner[start] == '0':
                    """q1 ke q2"""
                    self.curr = self.role[1]
                    print(f"{self.biner[start]} -> {self.curr}")
                    return self.circle(start+1, finish, False)
                else:
                    """q1 ke q3"""
                    self.curr = self.role[2]
                    print(f"{self.biner[start]} -> {self.curr}")
                    return self.circle(start+1, finish, True)
            
            if self.curr == self.role[1]:
                if self.biner[start] == '0' or self.biner[start] == '1':
                    """q2 ke q1"""
                    self.curr = self.role[0]
                    print(f"{self.biner[start]} -> {self.curr}")
                    return self.circle(start+1, finish, False)

            if self.curr == self.role[2]:
                if self.biner[start] == '0':
                    """tetep di q3"""
                    print(f"{self.biner[start]} -> {self.curr}")
                    return self.circle(start+1, finish, True)
                else:
                    """q3 ke q2"""
                    self.curr = self.role[1]
                    print(f"{self.biner[start]} -> {self.curr}")
                    return self.circle(start+1, finish, False)

        else:
            return tentu

    def cek(self, curr, jum):
        """Ngecek Format. Format input harus berupa biner"""
        if curr < jum:
            if self.biner[curr] == '0' or self.biner[curr] == '1':
                return self.cek(curr+1, jum)
            else:
                return False
        else:
            return True

    def baca(self):
        """Ngecek apakah string biner sesuai kriteria"""
        if self.cek(0, len(self.biner)) is True:
            if self.circle(0, len(self.biner), False) is True:
                print("Sesuai Kriteria")
            else:
                print("Tidak Sesuai Kriteria")
        else:
            print("SALAH FORMAT!!")

if __name__ == '__main__':
    ambil = input()
    mesin = MesinGabut(ambil)

    mesin.baca()