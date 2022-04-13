import array

if __name__ == '__main__':
    x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    t = tuple(ord(symbol) for symbol in x)
    a = array.array("I", (ord(symbol) for symbol in x))
    print(t)
    print(a)