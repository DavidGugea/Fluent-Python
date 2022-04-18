from array import array
from random import random

if __name__ == '__main__':
    floats = array('d', (random() for i in range(10 ** 7)))
    print(floats[-1])

    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()
