def validBraces(string):
    string = list(string)
    opposite = {'(': ')', '[': ']', '{': '}'}
    idx = 0
    while idx < len(string) - 1:
        if string[idx] in opposite.keys():
            if string[idx + 1] == opposite[string[idx]]:
                string.pop(idx)
                string.pop(idx)
                idx = 0
            else:
                idx += 1
        else:
            idx += 1
    else:
        if len(string) > 0:
            return False
        else:
            return True
