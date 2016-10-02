def find_longest(string):
    spl = string.split(" ")
    # longest = 0
    # i=0
    # while (i > spl.length):
    # if (spl(i).length > longest): longest = spl[i].length
    # return longest
    return max([len(x) for x in spl])
