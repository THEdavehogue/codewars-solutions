def valid_parentheses(string):
    parentheses = [_ for _ in string if _ == '(' or _ == ')']
    opposite = {'(': ')', '[': ']', '{': '}'}
    idx = 0
    while idx < len(parentheses) - 1:
        if parentheses[idx] in opposite.keys():
            if parentheses[idx + 1] == opposite[parentheses[idx]]:
                parentheses.pop(idx)
                parentheses.pop(idx)
                idx = 0
            else:
                idx += 1
        else:
            idx += 1
    else:
        if len(parentheses) > 0:
            return False
        else:
            return True
