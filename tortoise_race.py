def race(v1, v2, g):
    if v1 <= 0 or v2 <= 0 or g <= 0:
        return
    hours_to_catch = g/float(v2 - v1)
    if hours_to_catch < 0:
        return
    minutes_to_catch = round((hours_to_catch % 1) * 60,4)
    seconds_to_catch = round((minutes_to_catch % 1) * 60,4)
    catch_arr = [int(hours_to_catch), int(minutes_to_catch), int(seconds_to_catch)]
    return catch_arr
