import os

if __name__ == '__main__':
    fp = open("cafe.txt", "w", encoding="utf-8")
    print(fp)  # 1. By default, >open< operators in text mode and returns a >TextIOWrapper< object.
    fp.write("café")  # 2. The write method on a >TextIOWrapper< returns the number of Unicode characters written.
    fp.close()

    print(os.stat("cafe.txt").st_size)  # 3.  >>os.stat<< reports that the file holds 5 bytes; UTF-8 encodes 'é' as 2 bytes, 0xc3 and 0xa9

    fp2 = open("cafe.txt")
    print(fp2)  # 4. Opening a text file with no explicit encoding returns a >TextIOWrapper< with the encoding set to a default from the locale
    print(fp2.encoding)  # 5.  A >TextIOWrapper< object has an encoding attribute that you can inspect: cp1252 in this case
    print(fp2.read())  # 6. In the Windows >cp1252< encoding, the bytes 0xc3 is an "A" ( A with tilde ) and 0xa9 is the copyright sign
    fp2.close()

    fp3 = open("cafe.txt", encoding="utf-8")  # 7. Opening the same file with the correct encoding
    print(fp3)
    print(fp3.read())  # 8. The expected result: the same four Unicode characters for 'café'
    fp3.close()

    fp4 = open("cafe.txt", "rb")  # 9. The >'rb'< flag opens a file for reading in binary mode
    print(fp4)  # 10. The returned object is a >BufferedReader< and not a >TextIOWrapper<
    print(fp4.read())  # 11. Reading that returns bytes, as expected
