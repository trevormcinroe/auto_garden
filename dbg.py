import datetime

print(datetime.datetime.now())

"""
2020_01_01_1425
"""

day, hour = str(datetime.datetime.now()).split(' ')

day = day.replace('-', '_')
hour = hour.split('.')[0].replace(':', '')

dte_str = day + "_" + hour
print(dte_str)

del day, hour
print(dte_str)