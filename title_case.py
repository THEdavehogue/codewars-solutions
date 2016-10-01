def title_case(title, minor_words=''):
    if title == '':
        return title
    words = title.lower().split()
    minor_word_list = minor_words.lower().split()
    index = 0
    title_case_lst = [word.capitalize() if word not in minor_word_list else word.lower()
                      for word in words]
    return (title_case_lst[0].capitalize() + ' ' + ' '.join(title_case_lst[1:])).strip()
