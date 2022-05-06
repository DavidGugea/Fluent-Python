from dis import dis, code_info

b = 6


def f1(a):
    print(a)
    print(b)


def f2(a):
    # global b

    print(a)
    print(b)
    b = 3


dis(f1)

print("-"*50)
for i in range(3):
    print()
print("-"*50)

dis(f2)