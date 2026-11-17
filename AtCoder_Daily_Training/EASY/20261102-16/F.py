# import numpy as np

# number = int(input())

# print(int(np.base_repr(number-1, 5)) * 2)

def base10int(value, base):
    if value // base:
        return base10int(value // base, base) + str(value % base)
    return str(value % base)

number = int(input())

print(int(base10int(number-1, 5)) * 2)
