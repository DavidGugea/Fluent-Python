if __name__ == '__main__':
    x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ord_list = [ord(i) for i in x]
    ord_list_even = [ord(i) for i in x if ord(i) % 2 == 0]
    print(ord_list)
    print(ord_list_even)
