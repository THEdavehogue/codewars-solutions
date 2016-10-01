def dirReduc(arr):
    idx = 0
    opposites = {'NORTH': 'SOUTH', 'EAST': 'WEST',
                 'SOUTH': 'NORTH', 'WEST': 'EAST'}
    while idx < len(arr) - 1:
        if arr[idx + 1] == opposites[arr[idx]]:
            arr.pop(idx)
            arr.pop(idx)
            idx = 0
        else:
            idx += 1
    else:
        return arr
