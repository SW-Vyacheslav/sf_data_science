import numpy as np

def any_normal(*vectors):
    vectors_count = len(vectors)

    for i in range(0,  vectors_count):
        for j in range(i + 1, vectors_count):
            dot_product = np.dot(vectors[i], vectors[j])

            if dot_product == 0.0:
                return True

    return False

vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])

print("True ==", any_normal(vec1, vec2, vec3))
