def formatted_name (first_name, last_name):
    full_name = first_name + ' ' +last_name
    return full_name
def car_speed (speed):
    if speed < 0:
        level = 'Invalid'
    if speed >= 0 & speed < 40:
        level = 'Low'
    if speed >= 40 & speed < 120:
        level = 'Normal'
    if speed >= 120 & speed < 200:
        level = 'High'
    if speed >= 200 & speed < 220:
        level = 'V.High'
    if speed > 220:
        level = 'Invalid'
    return level

