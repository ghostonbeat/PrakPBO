class MesinGabut():
    def __init__(self, biner):
        self.biner = biner

    def cek(self):
        if self.biner[0] == '0' or self.biner[0] == '1':
            for i in range(len(self.biner)):
                print(self.biner[i])

if __name__ == '__main__':
    ambil = input()
    mulai = MesinGabut(ambil)
    mulai.cek()