def formatted_name (first_name, last_name):
    full_name = first_name + ' ' +last_name
    return full_name
def car_speed (speed):
         if speed < 0:
            return 'Invalid'
         elif speed >= 0 and speed < 40:
            return 'Low'
         elif speed >= 40 and speed < 120:
            return 'Normal'
         elif speed >= 120 and speed < 200:
            return 'High'
         elif speed >= 200 and speed < 220:
            return 'V.High'
         else :
            return 'Invalid'


