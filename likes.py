def likes(names):
    num_likes = len(names)
    if num_likes == 0:
        return 'no one likes this'
    elif num_likes == 1:
        return '%s likes this' % (names[0])
    elif num_likes == 2:
        return '%s and %s like this' % (names[0], names[1])
    elif num_likes == 3:
        return '%s, %s and %s like this' % (names[0], names[1], names[2])
    else:
        return '%s, %s and %s others like this' % (names[0], names[1], str(num_likes - 2))
