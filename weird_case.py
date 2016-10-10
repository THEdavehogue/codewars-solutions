def to_weird_case(string):
    '''
    Examples:

    to_weird_case('String'); # => returns 'StRiNg'
    to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
    '''
    result = ''
    for word in string.split():
        for i, char in enumerate(word):
            if not i % 2:
                result += char.upper()
            else:
                result += char.lower()
        result += ' '
    return result.strip()
