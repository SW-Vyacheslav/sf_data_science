import numpy as np

def get_loto(num):
    return np.random.randint(0, 101, (num, 5, 5))

def get_unique_loto(num):
    array = np.empty((num, 5, 5))

    for i in range(num):
        array[i] = np.random.choice(101, (5, 5), False)

    return array

#print(get_loto(3))
print(get_unique_loto(3))
