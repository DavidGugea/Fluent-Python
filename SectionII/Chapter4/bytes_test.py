if __name__ == '__main__':
    cafe = bytes("hellö wörld", encoding='utf-8')
    print(cafe)
    print(cafe[0])
    print(cafe[-1])
    cafe_arr = bytearray(cafe)
    print(cafe_arr)
    print(cafe_arr[-1])

    print(bytes.fromhex('31 4B CE A9'))