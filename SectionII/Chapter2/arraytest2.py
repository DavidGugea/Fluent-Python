from array import array

x = array('I')

x.fromlist(list(range(1, 6)))
print(x)
print(x.tobytes())
print(x)
x.frombytes(x.tobytes())
print(x)