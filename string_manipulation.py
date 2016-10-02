def pop_shift(strn):
    str_lst = [char for char in strn]
    str_mid = len(strn) // 2
    str_1 = []
    str_2 = []
    for i in range(str_mid):
        str_1.append(str_lst.pop(-1))
        str_2.append(str_lst.pop(0))
    return [''.join(str_1), ''.join(str_2), ''.join(str_lst)]

# 10 minute sprint
