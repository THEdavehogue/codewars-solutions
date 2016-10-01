def format_duration(seconds):
    if not seconds:
        return 'now'
    duration_lst = []
    duration = ''
    units = {'y': 'year', 'd': 'day',
             'h': 'hour', 'm': 'minute', 's': 'second'}
    s = seconds % 60
    m = (seconds / 60) % 60
    h = (seconds / 3600) % 24
    d = (seconds / 86400) % 365
    y = (seconds / 31536000)
    lst = [y, d, h, m, s]
    for unit in lst:
        if unit == 1:
            duration_lst.append('{} {}'.format(unit, units[unit]))
        elif unit > 1:
            duration_lst.append('{} {}s'.format(unit, units[unit]))
    for idx, string in enumerate(duration_lst):
        duration += string
        if idx < len(duration_lst) - 2:
            duration += ', '
        elif idx == len(duration_lst) - 2:
            duration += ' and '
    return duration
