import numpy as np


def comp(array1, array2):
    if type(array1) == type(array2):
        a1 = np.array(array1)
        a2 = np.array(array2)
        print(array1, array2, a1, a2)
        return sorted(a1**2) == sorted(a2)
    return False
