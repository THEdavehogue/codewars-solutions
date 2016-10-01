def string_clean(s):
    """
    Function will return the cleaned string (removing numeric chars)
    """
    nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    return ''.join([_ for _ in s if _ not in nums])
