import re


def to_camel_case(text):
    words = [word for word in re.split('-|_', text)]
    return ''.join([word.capitalize() if idx > 0 else word
                    for idx, word in enumerate(words)])
