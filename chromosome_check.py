def chromosome_check(sperm):
    '''
    INPUT: String, either 'XX' or 'XY'. 
    OUTPUT: Returns boy or girl message depending on input string
    '''
    boy = 'Congratulations! You\'re going to have a son.'
    girl = 'Congratulations! You\'re going to have a daughter.'
    return boy if 'Y' in sperm else girl
