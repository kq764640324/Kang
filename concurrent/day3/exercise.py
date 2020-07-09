from multiprocessing import Process
import os

size = os.path.getsize("day03.txt")
# print(f.tell())

def up_copy():
    f = open("day03.txt", "rb")
    s = open("day03_up.txt", "wb")
    n = size // 2
    while True:
        if size  >= 1024:
            data = f.read(1024)
            n  -= 1024
            if n < 0:
                f.seek(-1024,1)
                data = f.read(n+1024)
                s.write(data)
                break
            s.write(data)
        else:
            data = f.read(n)
            s.write(data)
            break

    f.close()
    s.close()



def down_coyp():
    f = open("day03.txt", "rb")
    s = open("day03_down.txt", "wb")
    f.seek(size//2)
    data = f.read()
    s.write(data)
    f.close()
    s.close()


# p1 = Process(target=up_copy)
# p2 = Process(target=down_coyp)
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()

up_copy()
down_coyp()
