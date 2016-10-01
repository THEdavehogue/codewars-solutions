class RomanNumerals(object):

    def __init__(self, value):
        self.value = value

    @classmethod
    def to_roman(self, n):
        roman_list = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                      (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        result = ''
        for x in roman_list:
            while n >= x[0]:
                result += x[1]
                n -= x[0]
        return result

    @classmethod
    def from_roman(self, roman):
        roman_dict = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arabic = 0
        digits = [i for i in roman[::-1]]
        for idx, digit in enumerate(digits):
            if idx == 0 or roman_dict[digit] >= roman_dict[digits[idx - 1]]:
                arabic += roman_dict[digit]
            else:
                arabic -= roman_dict[digit]
        return arabic
