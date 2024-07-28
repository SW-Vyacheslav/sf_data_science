import numpy as np
import math

def vec_dist(v1, v2):
    x = v2[0] - v1[0]
    y = v2[1] - v1[1]
    z = v2[2] - v1[2]

    return math.sqrt(x * x + y * y + z * z)

def min_max_dist(*vectors):
    max_dist = -np.finfo(np.float32).max
    min_dist = np.finfo(np.float32).max

    vectors_count = len(vectors)

    for i in range(0,  vectors_count):
        for j in range(i + 1, vectors_count):
            dist = vec_dist(vectors[i], vectors[j])

            if dist < min_dist:
                min_dist = dist

            if dist > max_dist:
                max_dist = dist

    return (min_dist, max_dist)


vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7,8,9])

print("(5.196152422706632, 10.392304845413264) ==", min_max_dist(vec1, vec2, vec3))
