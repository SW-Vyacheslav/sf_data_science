import numpy as np

def shuffle_seed(arr: list):
    high_seed = 2**32-1
    seed = np.random.rand() * high_seed
    np.random.seed(np.uint64(seed))

    shuffled_array = arr.copy()
    np.random.shuffle(shuffled_array)

    return (shuffled_array, seed)


array = [1, 2, 3, 4, 5]
print(shuffle_seed(array))
print(shuffle_seed(array))
