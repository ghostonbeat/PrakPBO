import threading
import time

class olah_data(threading.Thread):
    def __init__(self, rentang):
        self.rentang = rentang
        super(olah_data, self).__init__()

    def take(self):
        print(f'[1] take --> {self.rentang}')
        time.sleep(2)
    
    def sort(self):
        print(f'[2] sort --> {self.rentang}')
        time.sleep(2)
    
    def export(self):
        print(f'[3] export --> {self.rentang}')
        time.sleep(2)

    def run(self):
        self.take()
        self.sort()
        self.export()

rents = [
    'xxx1', 'xxx2', 'xxx3', 'xxx4'
]

start = time.perf_counter()
for rentang in rents:
    t = olah_data(rentang)
    t.start()
t.join()
finish = time.perf_counter()
print(f'selesai dalam {finish - start} detik')