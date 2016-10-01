import numpy as np


def determinant(matrix):
    return round(np.linalg.det(np.array(matrix)), 0)
