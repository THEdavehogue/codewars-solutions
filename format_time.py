def make_readable(seconds):
    h = (seconds / 3600) % 100
    m = (seconds / 60) % 60
    s = seconds % 60
    print h, m, s
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)
