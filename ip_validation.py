def is_valid_IP(strng):
    splits = strng.split('.')
    if len(splits) != 4:
        return False
    if splits[3] == '0':
        return False
    for x in splits:
        if x.isdigit() and x[0] != '0':
            if int(x) < 256:
                continue
            else:
                return False
        else:
            return False
    return True
