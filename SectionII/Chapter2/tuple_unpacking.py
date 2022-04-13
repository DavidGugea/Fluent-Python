import os

if __name__ == '__main__':
    x, y = (5, 10)
    _, filename = os.path.split("testfolder/test.py")
    print(filename)
    print(x, y)
