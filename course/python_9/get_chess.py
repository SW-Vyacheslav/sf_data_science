import numpy as np

def get_chess(a):
    if a <= 0:
        raise ValueError("Invalid \'a\' value. Value must be greater than 0")

    arr = np.zeros((a, a))

    if a != 1:
        if (a % 2 == 0):
            arr[::2, ::-2] = 1
            arr[::-2, ::2] = 1
        else:
            arr[1::2, ::-2] = 1
            arr[::-2, 1::2] = 1

    return arr

for i in range(1, 7):
    print(i, ":\n", get_chess(i))
