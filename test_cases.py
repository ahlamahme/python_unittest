def formatted_name (first_name, last_name):
    full_name = first_name + ' ' +last_name
    return full_name
def car_speed (speed):
    if speed < 0:
        level = 'Invalid'
    elif speed >= 0 & speed < 40:
        level = 'Low'
    elif speed >= 40 & speed < 120:
        level = 'Normal'
    elif speed >= 120 & speed < 200:
        level = 'High'
    elif speed >= 200 & speed < 220:
        level = 'V.High'
    elif speed > 220:
        level = 'Invalid'
    return level

